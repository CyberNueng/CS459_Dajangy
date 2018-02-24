from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    model=models.CharField(max_length=30)
    detail=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

class Rent(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    car=models.ForeignKey(Car, on_delete=models.CASCADE)
    start_datetime=models.DateTimeField()
    return_time=models.DateTimeField()
    fee=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)