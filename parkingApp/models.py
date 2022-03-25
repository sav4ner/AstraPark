import email
from os import name
from pyexpat import model
from statistics import mode
from tracemalloc import stop
from django.db import models
from matplotlib.cbook import print_cycles
from sqlalchemy import false, true

# Create your models here.
class cartype(models.Model):
    types = models.CharField(primary_key=True,max_length=100)

class carstate(models.Model):
    states = models.CharField(primary_key=True, max_length=50)

class status(models.Model):
    state = models.CharField(primary_key=True, max_length=150)

class premises(models.Model):
    name = models.CharField(primary_key=True,max_length=300)
    space = models.IntegerField(default=10)

class lots(models.Model):
    lotId = models.AutoField(primary_key=True)
    area = models.CharField(max_length=150)
    location = models.CharField(max_length=300)
    premises = models.ForeignKey(premises,default=' ',related_name="premis",on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    price = models.PositiveIntegerField()
    status = models.ForeignKey(status,related_name='stat',on_delete=models.CASCADE)

class bookings(models.Model):
    bookingId = models.AutoField(primary_key=True)
    user= models.CharField(max_length=150)
    platenumber = models.CharField(max_length= 150)
    email = models.EmailField(null=False)
    contact = models.CharField(max_length=100)
    date= models.DateField()
    start= models.TimeField()
    stop = models.TimeField()
    lots= models.ForeignKey(lots,related_name='Lot', on_delete=models.CASCADE)
    bill = models.PositiveIntegerField()

class car(models.Model):
    platenumber = models.CharField(primary_key=True,max_length=150)
    owner = models.CharField(max_length=150)
    carstate = models.ForeignKey(carstate,related_name="state",on_delete=models.CASCADE)
    cartype = models.ForeignKey(cartype,related_name="type",on_delete=models.CASCADE)

class businessusers(models.Model):
    businessId = models.AutoField(primary_key=True)
    user = models.CharField(max_length=150)
    premises = models.ForeignKey(premises,related_name="prem",on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    dividents = models.IntegerField(default=0)

class favourites(models.Model):
    lotId = models.ForeignKey(lots,related_name="fav", on_delete=models.CASCADE)
    user = models.CharField(max_length=150,default='')
