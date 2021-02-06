from django.urls import path
from .views import FlightList, AirportList, StaffList,EmployeeList,PassengerList
urlpatterns = [
    path('', AirportList.as_view()),
    path('flight/', FlightList.as_view()),
    path('staff/', StaffList.as_view()),
    path('em/', EmployeeList.as_view()),
    path('passenger/', PassengerList.as_view()),
]
