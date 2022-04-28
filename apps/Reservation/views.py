# django
from django.views.generic import CreateView

# my app
from .models import Reservation
from .forms import ReservationForm

# Create your views here.

class ReservationCreateView(CreateView):
    model = Reservation
    template_name = "reservation/reservation_create.html"
    form_class = ReservationForm
