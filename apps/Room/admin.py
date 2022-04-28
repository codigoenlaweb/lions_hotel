# django
from django.contrib import admin

# my app
from .models import Room

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    '''Admin View for Room'''

    list_display = ('type_of_room', 'room_number', 'floor_number',)
    list_filter = ('type_of_room', 'floor_number',)
    search_fields = ('room_number',)
    ordering = ('type_of_room',)
    list_per_page = 25
    