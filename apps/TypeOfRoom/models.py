from django.db import models

# Create your models here.

# Type Of Room models
class TypeOfRoom(models.Model):
    """Model definition for TypeOfRoom."""

    # fields here
    category = models.CharField(verbose_name="Category", max_length=20)
    number_of_people = models.IntegerField(verbose_name="Number of people")
    price = models.DecimalField(verbose_name="Price", max_digits=5, decimal_places=2)
    


    class Meta:
        """Meta definition for TypeOfRoom."""

        verbose_name = 'TypeOfRoom'
        verbose_name_plural = 'TypeOfRooms'

    def __str__(self):
        """Unicode representation of TypeOfRoom."""
        return self.category + ' - ' + str(self.price) + '€'