from django.db import models
from django.contrib.auth.models import User
from django.views.generic.list import ListView

# Create your models here.
class Car(models.Model):
	model=models.CharField(max_length=20)
	detail=models.CharField(max_length=100)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	def __str__(self):
		return "id: %s, model: %s, price: %s"%(self.id, self.model, self.price)

class Customer(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	phone=models.CharField(max_length=20)
	def __str__(self):
		return "id: {}, {}".format(self.id, self.first_name)

class Rent(models.Model):
	customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
	car=models.ForeignKey(Car, on_delete=models.CASCADE)
	start=models.DateTimeField()
	stop=models.DateTimeField()
	fee=models.DecimalField(max_digits=10,decimal_places=2)
