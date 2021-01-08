from django.contrib import admin

# Register your models here.
from .models import Staff , Flight ,Airport ,Passenger ,Tickets , Employee

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Tickets)
admin.site.register(Employee)
