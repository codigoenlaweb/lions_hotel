from django.db import models
from django.db.models import Q


class RoomManager(models.Manager):

    def rooms_available(self, category, entry_date, deperture_date):
        if entry_date == "" or deperture_date == "":
            return self.filter(type_of_room__number_of_people=0)
        else:
            return self.filter(type_of_room=category).exclude(Q(reservation_room__entry_date__range=[entry_date, deperture_date]) | Q(reservation_room__deperture_date__range=[entry_date, deperture_date])).exclude(reservation_room__entry_date__lte=entry_date, reservation_room__deperture_date__gte=deperture_date)



