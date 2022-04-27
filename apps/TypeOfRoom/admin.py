# django
from django.contrib import admin

# my app
from .models import TypeOfRoom

# Register your models here.
@admin.register(TypeOfRoom)
class TypeOfRoomAdmin(admin.ModelAdmin):
    '''Admin View for TypeOfRoom'''

    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)