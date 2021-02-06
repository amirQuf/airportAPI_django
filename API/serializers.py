from airport.models import  Airport,Flight,Staff,Employee,Passenger,Tickets
from rest_framework import serializers


class AirportSerializer(serializers.ModelSerializer):
  class Meta:
    model = Airport
    fields = ("name","city","country")


class FlightSerializer(serializers.ModelSerializer):
  class Meta:
    model = Flight
    fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
  class Meta:
    model = Staff
    fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'
