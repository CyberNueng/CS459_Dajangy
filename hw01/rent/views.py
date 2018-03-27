from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import Car
from rest_framework import viewsets
from rest_framework.response import Response
from rent.serializers import CustomerSerializer, CarSerializer, RentSerializer
from rent.models import Customer, Rent

# Create your views here.
class CarListView(ListView):
    model = Car
    template_name='list.html'

class HomeView(TemplateView):
    template_name='home.html'

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.first_name = request.data.get("first_name")
        instance.last_name = request.data.get("last_name")
        instance.phone = request.data.get("phone")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.validated_data
        instance.save()

        self.perform_update(serializer)

        return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer