# django
from django.db import models

# my app
from apps.Room.models import Room
from apps.TypeOfRoom.models import TypeOfRoom

# Third party apps
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Reservation(models.Model):
    """Model definition for Reservation."""

    # fields here
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE)
    reservation_date = models.DateField(verbose_name="Reservation date", auto_now_add=True)
    entry_date = models.DateField(verbose_name="Entry date")
    deperture_date = models.DateField(verbose_name="Deperture date")
    guest_number = models.IntegerField(verbose_name="Guest number")
    name_of_person = models.CharField(verbose_name="Name of Person", max_length=50)
    email_of_person = models.EmailField(verbose_name="Email of Person", max_length=250)
    phone_number_person = PhoneNumberField(unique =False, null = False, blank = False)
    total_price = models.DecimalField(verbose_name="Toal price", max_digits=6, decimal_places=2)
    localizador = models.CharField(verbose_name="Localizador", max_length=8)

    class Meta:
        """Meta definition for Reservation."""

        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        """Unicode representation of Reservation."""
        return str(self.room) + ' - ' + str(self.entry_date) + ' - ' + str(self.deperture_date) + ' - ' + self.name_of_person