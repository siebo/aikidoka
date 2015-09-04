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
          ('1dan', 'shodan (1st Dan)'),
          ('2dan', 'nidan (2nd Dan)'),
          ('3dan', 'sandan (3rd Dan)'),
          ('4dan', 'yondan (4th Dan)'),
          ('5dan', 'godan (5th Dan)'),
          ('6dan', 'rokudan (6th Dan)'),
          ('7dan', 'shichidan (7th Dan)'),
          ('8dan', 'hachidan (8th Dan)'),
      )

    first_name = models.CharField(
        max_length=32,
    )

    last_name = models.CharField(
        max_length=32,
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
        max_length=32,
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