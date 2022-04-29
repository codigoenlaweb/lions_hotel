# django
from datetime import date
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
        fields = ('room','entry_date', 'deperture_date', 'guest_number',
                  'name_of_person', 'email_of_person', 'phone_number_person',)
    
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['guest_number'].widget.attrs.update({'placeholder': 'People number'})
        self.fields['name_of_person'].widget.attrs.update({'placeholder': 'Name of owner'})
        self.fields['email_of_person'].widget.attrs.update({'placeholder': 'Email of owner'})
        self.fields['phone_number_person'].widget.attrs.update({'placeholder': 'Phone number of owner'})
        
    def clean(self):
        # get data
        cleaned_data = super(ReservationForm, self).clean()
        entry_date = cleaned_data.get("entry_date")
        deperture_date = cleaned_data.get("deperture_date")
        id_room = cleaned_data.get("room")
        name_of_person = cleaned_data.get("name_of_person")
        
        # validation room avaible
        room_avaible = Room.objects.rooms_available_valid(id_room.id, entry_date, deperture_date)
        if len(room_avaible) != 1:
            print(room_avaible)
            raise forms.ValidationError({'entry_date':('reservation error.')})
        
        # entry cannot be less than the current date
        if entry_date <= date.today():
            raise ValidationError({'entry_date':('date must be greater than current date.')})
        
        # deperture cannot be less than the current date
        if deperture_date <= date.today():
            raise ValidationError({'deperture_date':('date must be greater than current date.')})
        
        # deperture cannot be less than the entry
        if deperture_date < entry_date:
            raise ValidationError({'deperture_date':('the departure date must be greater than the arrival date.')})
        
        # deperture cannot be lees than the 31/12/2022
        if deperture_date > date(year=2022, month=12, day=31):
            raise ValidationError({'deperture_date':('the departure date must be less than 12-31-2022.')})
        
        # the name cannot be lees than to 2 character
        if len(name_of_person) < 2:
            raise ValidationError({'name_of_person':('the name is too short.')})
    