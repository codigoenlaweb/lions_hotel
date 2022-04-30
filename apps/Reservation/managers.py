#django
from django.db import models

# managaers
class ReservationManager(models.Manager):
    
    def search_locator(self, localizador):
        if localizador == None:
            localizador = ""
        
        return self.filter(localizador=localizador, confirmed=True)
        