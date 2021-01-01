from django.db import models
from django.utils import timezone

class Airport(models.Model):
  name = models.CharField(max_length=60,unique=True)
  city  = models.CharField(max_length=60)
  country = models.CharField(max_length=60)
  def __str__(self):
    return self.name 


class Flight(models.Model):
  orgin = models.ForeignKey(Airport, related_name='orgin',on_delete = models.CASCADE)
  destination = models.ForeignKey(Airport, related_name='destination' , on_delete=models.CASCADE)
  flight_time = models.DateTimeField(default=timezone.now)
  land_time = models.DateTimeField(default=timezone.now)
  status = models.CharField(max_length=3)
  capcity  = models.IntegerField()
  def __str__(self):
    return f"{orgin.name}to{destination.name}"

class  Staff(models.Model):
  name = models.CharField(max_length=60)
  age  = models.IntegerField()
  role = models.CharField(max_length=10)
  mobile = models.CharField(max_length=11)
  gender = models.CharField(max_length=1)
  flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

