# python
from datetime import date

# django
from django.views.generic import DetailView
from django.urls import reverse_lazy

# my app
from .models import TypeOfRoom
from apps.Room.models import Room

# Create your views here.

class RoomAvaibleDetailView(DetailView):
    context_object_name = 'type_of_room'
    model = TypeOfRoom
    template_name = "type_of_room/room_avaible.html"
    success_url = reverse_lazy("home:dashboard")
    
    def get_context_data(self,**kwargs):
        context = super(RoomAvaibleDetailView, self).get_context_data(**kwargs)
        # get room type id
        category = self.kwargs.get('pk')
        # get date entry and deperture
        entry_date = self.request.GET.get('entry_date') 
        deperture_date = self.request.GET.get('deperture_date')
   
        
        if entry_date != None:
            if entry_date >= deperture_date:
                context['date_error'] = 'the check-in date cannot be less than the check-out date'
            else:
                # room avaible
                context['room_avaible'] = Room.objects.rooms_available(category, entry_date, deperture_date)
            
        context['min_date'] = date.today().strftime("%Y-%m-%d")
        context['entry_date'] = entry_date
        context['deperture_date'] = deperture_date
        return context
    
    
    

