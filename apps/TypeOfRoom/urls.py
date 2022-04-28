from django.urls import path
from .views import *

app_name = 'type_of_reservation'
urlpatterns = [
    path('<pk>/', RoomAvaibleDetailView.as_view(), name="room_avaible"),
]
