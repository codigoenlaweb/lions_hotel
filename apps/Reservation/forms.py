# django
from django import forms

# my app
from .models import Reservation

# forms from Reservation
class ReservationForm(forms.ModelForm):
    """Form definition for Reservation."""

    class Meta:
        """Meta definition for Reservationform."""

        model = Reservation
        fields = ('__all__')
