from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory
from .models import Aikidoka
from .views import ListAikidokaView

class AikidokaTests(TestCase):
    """Aikidoka model tests."""
    
    def test_str(self):
        aikidoka = Aikidoka(first_name='Morihiro', last_name='Saito')
        self.assertEquals(
            str(aikidoka),
            'Morihiro Saito',
    )

class AikidokaListViewTests(TestCase):
    """Aikidoka list view tests."""

    def test_aikidoka_in_the_context(self): 

        client = Client()
        response = client.get('/')

        self.assertEquals(list(response.context['object_list']), [])

        Aikidoka.objects.create(first_name='Gozo', last_name='Shioda')
        response = client.get('/')
        self.assertEquals(response.context['object_list'].count(), 1)

    def test_aikidoka_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = ListAikidokaView.as_view()(request)

        self.assertEquals(list(response.context_data['object_list']), [])

        Aikidoka.objects.create(first_name='Moriteru', last_name='Ueshiba')
        response = ListAikidokaView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)