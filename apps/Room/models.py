# django
from django.db import models

# my app
from apps.TypeOfRoom.models import TypeOfRoom

# Create your models here.
    
# Room models
class Room(models.Model):
    """Model definition for Room."""
    
    # fields here
    type_of_room = models.ForeignKey(TypeOfRoom, verbose_name="Type Of Room", on_delete=models.CASCADE) 
    room_number = models.CharField(verbose_name="Room number", max_length=6, unique=True)
    floor_number = models.CharField(verbose_name="Floor number", max_length=12)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    

    
    class Meta:
        """Meta definition for Room."""
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        """Unicode representation of Room."""
        return str(self.type_of_room) + ' - ' + self.room_number + ' - ' + self.floor_number
    

