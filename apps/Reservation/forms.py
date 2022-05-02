# python
from datetime import date, datetime, timezone, timedelta

# django
from django import forms
from django.core.exceptions import ValidationError

# my app
from .models import Reservation
from apps.Room.models import Room
# forms from Reservation


class ReservationForm(forms.ModelForm):
    """Form definition for Reservation."""

    class Meta:
        """Meta definition for Reservationform."""
        model = Reservation
        fields = ('room', 'entry_date', 'deperture_date', 'guest_number',
                  'name_of_person', 'email_of_person', 'phone_number_person',)

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['guest_number'].widget.attrs.update(
            {
                'placeholder': 'People number',
                'class': 'w-full h-10 mb-4 bg-secondarygray rounded px-2 text-textinputfield font-bold outline-principalgreen outline-2 placeholder:text-gray-400'
            }
        )
        self.fields['name_of_person'].widget.attrs.update(
            {
                'placeholder': 'Name of owner',
                'class': 'w-full h-10 mb-4 bg-secondarygray rounded px-2 text-textinputfield font-bold outline-principalgreen outline-2 placeholder:text-gray-400'
            }
        )
        self.fields['email_of_person'].widget.attrs.update(
            {
                'placeholder': 'Email of owner',
                'class': 'w-full h-10 mb-4 bg-secondarygray rounded px-2 text-textinputfield font-bold outline-principalgreen outline-2 placeholder:text-gray-400'
            }
        )
        self.fields['phone_number_person'].widget.attrs.update(
            {
                'placeholder': 'Phone number of owner',
                'class':"hidden"
            }
        )

    def clean(self):
        # get data
        cleaned_data = super(ReservationForm, self).clean()
        entry_date = cleaned_data.get("entry_date")
        deperture_date = cleaned_data.get("deperture_date")
        id_room = cleaned_data.get("room")
        name_of_person = cleaned_data.get("name_of_person")

        # validation room avaible
        room_avaible = Room.objects.rooms_available_valid(
            id_room.id, entry_date, deperture_date)
        if len(room_avaible) != 1:
            print(room_avaible)
            raise forms.ValidationError({'entry_date': ('reservation error.')})

        # entry cannot be less than the current date
        if entry_date < date.today():
            raise ValidationError(
                {'entry_date': ('date must be greater than current date.')})

        # deperture cannot be less than the current date
        if deperture_date <= date.today():
            raise ValidationError(
                {'deperture_date': ('date must be greater than current date.')})

        # deperture cannot be less than the entry
        if deperture_date < entry_date:
            raise ValidationError({'deperture_date': (
                'the departure date must be greater than the arrival date.')})

        # deperture cannot be lees than the 31/12/2022
        if deperture_date > date(year=2022, month=12, day=31):
            raise ValidationError(
                {'deperture_date': ('the departure date must be less than 12-31-2022.')})

        # the name cannot be lees than to 2 character
        if len(name_of_person) < 2:
            raise ValidationError(
                {'name_of_person': ('the name is too short.')})


class ReservationConfirmForm(forms.ModelForm):
    code = forms.CharField()
    id_reservation = forms.CharField()

    class Meta:
        """Meta definition for Reservationform."""
        model = Reservation
        fields = ['confirmed', ]

    def clean(self):
        cleaned_data = super(ReservationConfirmForm, self).clean()
        code = cleaned_data.get("code")
        id_reservation = cleaned_data.get("id_reservation")
        is_equal_code_confirm = Reservation.objects.filter(
            id=id_reservation, confirmation_code=code)
        
        # if it brings me a list with more or less than one element, shoot error
        if len(is_equal_code_confirm) != 1:
            raise ValidationError(
                {'code': ('Your verification code is incorrect. Please note the capital letters')})

        # if the time limit exceeds 10 minutes, throw error
        # time limit
        time_limit = (datetime.now(timezone.utc) -
                      is_equal_code_confirm[0].confirmation_code_time)
        
        if time_limit > timedelta(minutes=10):
            raise ValidationError({'code': (
                'Sorry, the time limit has been exceeded. Please, if you wish to reserve, we ask you to repeat the reservation process.')})

# reseend email


class ReseendEmailForm(forms.ModelForm):
    id_reservation = forms.CharField()

    class Meta:
        """Meta definition for Reservationform."""
        model = Reservation
        fields = ['confirmation_code', ]

    def clean(self):
        cleaned_data = super(ReseendEmailForm, self).clean()
        id_reservation = cleaned_data.get("id_reservation")
        is_equal_code_confirm = Reservation.objects.filter(id=id_reservation)

        # time limit
        time_limit = (datetime.now(timezone.utc) -
                      is_equal_code_confirm[0].confirmation_code_time)

        # if the time limit exceeds 10 minutes, throw error
        if time_limit > timedelta(minutes=10):
            raise ValidationError({'confirmation_code': (
                'Sorry, the time limit has been exceeded. Please, if you wish to reserve, we ask you to repeat the reservation process.')})
