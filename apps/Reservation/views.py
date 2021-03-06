# python
from datetime import datetime
import email

# django
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
import threading

# my app
from .models import Reservation
from .forms import ReservationConfirmForm, ReservationForm, ReseendEmailForm
from .utils import code_generator
from .email import create_reservation_email, localizador_email

# Create your views here.


class ReservationCreateView(CreateView):
    model = Reservation
    template_name = "reservation/reservation_create.html"
    form_class = ReservationForm
    # success_url = reverse_lazy("")

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

        # send email
        thread = threading.Thread(target=create_reservation_email, args=(self, reservation.email_of_person, reservation.confirmation_code))
        thread.start()
        # create_reservation_email(
        #     self=self,
        #     email_of_person=reservation.email_of_person,
        #     confirmation_code=reservation.confirmation_code,
        # )

        # success_url = reverse("reservation:confirm_reservation", kwargs={"pk": reservation})
        return super(ReservationCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ReservationCreateView, self).get_context_data(**kwargs)

        # get date entry and deperture
        context['entry_date'] = self.request.GET.get('entry_date')
        context['deperture_date'] = self.request.GET.get('deperture_date')

        # get id room
        context['id_room'] = self.request.GET.get('id_room')

        return context

    def get_success_url(self):
        return reverse('reservation:confirm_reservation', kwargs={'pk': self.object.id})


class ReservationUpdateView(UpdateView):
    context_object_name = 'reservation'
    model = Reservation
    template_name = "reservation/confirm_reservation.html"
    form_class = ReservationConfirmForm
    success_url = reverse_lazy("reservation:confirmed_reservations_list")

    def form_valid(self, form):
        # save commit false
        reservation = form.save(commit=False)

        # set reservation confirm
        reservation.confirmed = True

        # reservation save
        reservation.save()
        thread = threading.Thread(target=create_reservation_email, args=(self, reservation.email_of_person, reservation.localizador))
        thread.start()
        # localizador_email(
        #     self=self,
        #     email_of_person=reservation.email_of_person,
        #     localizador=reservation.localizador
        # )
        
        messages.success(self.request, 'Your reservation has been successful, we have sent you a locator code to your email')

        return super(ReservationUpdateView, self).form_valid(form)


class ReservationCodeConfirmUpdateView(UpdateView):
    context_object_name = 'reservation'
    model = Reservation
    template_name = "reservation/reseendemail.html"
    form_class = ReseendEmailForm

    def form_valid(self, form):
        # save commit false
        reservation = form.save(commit=False)

        # set reservation confirm
        reservation.confirmation_code = code_generator(size=5)

        # reservation save
        reservation.save()

        # send email
        thread = threading.Thread(target=create_reservation_email, args=(self, reservation.email_of_person, reservation.confirmation_code))
        thread.start()
        # create_reservation_email(
        #     self=self,
        #     email_of_person=reservation.email_of_person,
        #     confirmation_code=reservation.confirmation_code,
        # )

        return super(ReservationCodeConfirmUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('reservation:confirm_reservation', kwargs={'pk': self.object.id})


class ReservationConfirmedListView(ListView):
    model = Reservation
    template_name = "reservation/confirmed_reservations_list.html"

    def get_context_data(self, **kwargs):
        context = super(
            ReservationConfirmedListView,
            self
        ).get_context_data(**kwargs)

        localizador = self.request.GET.get('localizador')

        if localizador != None:
            your_reservation = Reservation.objects.search_locator(
                localizador
            )
            if len(your_reservation) == 1:
                context['your_reservation'] = your_reservation
            else:
                context['error'] = "Your locator code does not match any, make sure you are writing in uppercase"

        return context
