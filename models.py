from django.db import models

# Create your models here.

class Aikidoka(models.Model):
  
    RANKS = (
          ('6kyu', '6th kyu'),
          ('5kyu', '5th kyu'),
          ('4kyu', '4th kyu'),
          ('3kyu', '3rd kyu'),
          ('2kyu', '2nd kyu'),
          ('1kyu', '1st kyu'),
      )

    first_name = models.CharField(
        max_length=255,
    )

    last_name = models.CharField(
        max_length=255,
    )

    rank = models.CharField(
        max_length=4,
        choices=RANKS,
        default='6kyu'
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