from django.db import models

# Create your models here.

class Aikidoka(models.Model):

    first_name = models.CharField(
        max_length=255,
    )

    last_name = models.CharField(
        max_length=255,
    )

    rank = models.CharField(
        max_length=8,
    )

    address = models.CharField(
        max_length=255,
    )

    city = models.CharField(
        max_length=255,
    )

    state = models.CharField(
        max_length=12,
    )

    postal_code = models.CharField(
        max_length=14,
    )

    country = models.CharField(
        max_length=32,
    )

    email = models.EmailField() 

    phone = models.CharField(
        max_length=16,
    )

    def __str__(self):
      return ' '.join([ 
         self.first_name, 
         self.last_name,
         ])