# python
from datetime import datetime

# django
from django.views.generic import CreateView
from django.urls import reverse_lazy

# my app
from .models import Reservation
from .forms import ReservationForm
from .utils import code_generator

# Create your views here.
class ReservationCreateView(CreateView):
    model = Reservation
    template_name = "reservation/reservation_create.html"
    form_class = ReservationForm
    success_url = reverse_lazy("home:dashboard")

    def form_valid(self, form):
        # save commit false
        reservation = form.save(commit=False)
        
        # total days of reservation
        total_day = reservation.deperture_date - reservation.entry_date
        
        # set form
        reservation.total_price = reservation.room.type_of_room.price * total_day.days
        reservation.confirmation_code_time = datetime.now()
        reservation.localizador = code_generator()
        reservation.confirmation_code = code_generator(size=5)
        
        # reservation save
        reservation.save()
        return super(ReservationCreateView, self).form_valid(form)
    
    
    def get_context_data(self,**kwargs):
        context = super(ReservationCreateView, self).get_context_data(**kwargs)
       
        # get date entry and deperture
        context['entry_date'] = self.request.GET.get('entry_date') 
        context['deperture_date'] = self.request.GET.get('deperture_date')
        
        # get id room
        context['id_room'] = self.request.GET.get('id_room') 
        
        return context