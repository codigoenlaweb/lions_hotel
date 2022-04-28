from django.urls import path
from .views import *

app_name = 'reservation'
urlpatterns = [
    path('register reservation',
         ReservationCreateView.as_view(),
         name='register_reservation'),
]
