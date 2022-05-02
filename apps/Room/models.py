# django
from django.db import models

# my app
from apps.TypeOfRoom.models import TypeOfRoom
from .managers import RoomManager

# Create your models here.
    
# Room models
class Room(models.Model):
    """Model definition for Room."""
    
    # fields here
    type_of_room = models.ForeignKey(TypeOfRoom, verbose_name="Type Of Room", on_delete=models.CASCADE, related_name="room_type_of_room") 
    room_number = models.CharField(verbose_name="Room number", max_length=6, unique=True)
    floor_number = models.CharField(verbose_name="Floor number", max_length=12)
    
    objects = RoomManager()
    
    class Meta:
        """Meta definition for Room."""
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        """Unicode representation of Room."""
        return self.room_number
    

