from django.shortcuts import render
from .serializers import AirportSerializer, FlightSerializer, StaffSerializer,EmployeeSerializer,PassengerSerializer
from rest_framework import generics
from airport.models import Airport, Flight, Staff, Employee, Passenger, Tickets

class AirportList(generics.ListCreateAPIView):
  queryset = Airport.objects.all()
  serializer_class = AirportSerializer


class FlightList(generics.ListCreateAPIView):
  queryset = Flight.objects.all()
  serializer_class = FlightSerializer


class StaffList(generics.ListCreateAPIView):
  queryset = Staff.objects.all()
  serializer_class = StaffSerializer


class EmployeeList(generics.ListCreateAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer


class PassengerList(generics.ListCreateAPIView):
  queryset = Passenger.objects.all()
  serializer_class = PassengerSerializer
