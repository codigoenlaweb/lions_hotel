# django
from django.views.generic import ListView

# my app
from apps.TypeOfRoom.models import TypeOfRoom

# Create your views here.

class DashboardListView(ListView):
    context_object_name = 'type_of_rooms'
    # model = Room
    template_name = "home/dashboard.html"
    
    def get_queryset(self):        
        queryset = TypeOfRoom.objects.all()
        return queryset