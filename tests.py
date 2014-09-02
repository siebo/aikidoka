from django.test import TestCase
from .models import Aikidoka


class AikidokaTests(TestCase):
    """Aikidoka model tests."""
    
    def test_str(self):
        aikidoka = Aikidoka(first_name='Morihiro', last_name='Saito')
        self.assertEquals(
            str(aikidoka),
            'Morihiro Saito',
    )