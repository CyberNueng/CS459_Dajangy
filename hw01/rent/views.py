from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Car

# Create your views here.
class CarListView(ListView):
    model = Car
    template_name='list.html'