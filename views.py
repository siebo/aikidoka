from django.shortcuts import render
from django.views.generic import ListView

from .models import Aikidoka

class ListAikidokaView(ListView):
    model = Aikidoka
    template_name = 'aikidoka_list.html'