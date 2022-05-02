from django.urls import path
from .views import *

app_name = 'reservation'
urlpatterns = [
    path(
        'register reservation',
        ReservationCreateView.as_view(),
        name='register_reservation'
    ),

    path(
        'confirm reservation/<pk>',
        ReservationUpdateView.as_view(),
        name='confirm_reservation'
    ),
    path(
        'reseend email/<pk>',
        ReservationCodeConfirmUpdateView.as_view(),
        name='reseend_email'
    ),

    path(
        'confirmedreservationslist',
        ReservationConfirmedListView.as_view(),
        name='confirmed_reservations_list'
    ),
]
