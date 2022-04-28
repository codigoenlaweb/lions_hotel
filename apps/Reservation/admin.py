from datetime import datetime
# django
from django.contrib import admin

# my app
from .models import Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    '''Admin View for Reservation'''

    list_display = ('number_room', 'type_room', 'name_of_person', 'email_of_person', 'phone_number_person', 'full_payment', 'entry_date', 'deperture_date', 'localizador', 'confirmed')
    list_filter = ('confirmed', 'room',)
    # inlines = [
    #     Inline,
    # ]
    raw_id_fields = ('room',)
    # readonly_fields = ('',)
    search_fields = ('localizador',)
    # date_hierarchy = ''
    ordering = ('reservation_date',)
    list_per_page = 20
    
    def number_room(self, obj):
        return 'room ' + str(obj.room)
    
    def full_payment(self, obj):
        return str(obj.total_price) + '€'
    
    def type_room(self, obj):
        return obj.room.type_of_room