from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Car
from rest_framework import viewsets
from rent.serializers import CustomerSerializer
from rent.models import Customer

# Create your views here.
class CarListView(ListView):
    model = Car
    template_name='list.html'

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer