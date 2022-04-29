# python
from datetime import date, datetime

# django
from django.db import models
from django.forms import ValidationError

# my app
from apps.Room.models import Room

# Third party apps
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Reservation(models.Model):
    """Model definition for Reservation."""

    # fields here
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE, related_name='reservation_room')
    reservation_date = models.DateField(verbose_name="Reservation date", auto_now_add=True)
    entry_date = models.DateField(verbose_name="Entry date")
    deperture_date = models.DateField(verbose_name="Deperture date")
    guest_number = models.IntegerField(verbose_name="Guest number")
    name_of_person = models.CharField(verbose_name="Name of Person", max_length=50, unique=False)
    email_of_person = models.EmailField(verbose_name="Email of Person", max_length=250, unique=False)
    phone_number_person = PhoneNumberField(unique =False, null = False, blank = False)
    total_price = models.DecimalField(verbose_name="Toal price", max_digits=6, decimal_places=2)
    localizador = models.CharField(verbose_name="Localizador", max_length=8)
    confirmed = models.BooleanField(verbose_name="Confirmed", default=False)
    confirmation_code = models.CharField(verbose_name="Confirmation_code", max_length=5)
    confirmation_code_time = models.DateTimeField(verbose_name="Confirmation code time")

    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        """Unicode representation of Reservation."""
        return str(self.room) + ' - ' + str(self.entry_date) + ' - ' + str(self.deperture_date) + ' - ' + self.name_of_person

    def clean(self):
        if self.entry_date < date.today():
            raise ValidationError({'entry_date':('date must be greater than current date.')})
        if self.deperture_date < date.today():
            raise ValidationError({'deperture_date':('date must be greater than current date.')})
        if self.deperture_date < self.entry_date:
            raise ValidationError({'deperture_date':('the departure date must be greater than the arrival date.')})
        if self.deperture_date > date(year=2022, month=12, day=31):
            raise ValidationError({'deperture_date':('the departure date must be less than 12-31-2022.')})
        if len(self.name_of_person) < 2:
            print(datetime.now())
            raise ValidationError({'name_of_person':('the name is too short.')})