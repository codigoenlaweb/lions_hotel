# django
from django.views.generic import ListView

# my app
from apps.TypeOfRoom.models import TypeOfRoom
from apps.Room.models import Room

# Create your views here.

class DashboardListView(ListView):
    context_object_name = 'type_of_rooms'
    template_name = "home/dashboard.html"
    
    def get_queryset(self):        
        queryset = TypeOfRoom.objects.all()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)

        # get leng room
        context['leng_room'] = Room.objects.count_rooms()
        return context