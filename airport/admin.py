from django.contrib import admin

# Register your models here.
from .models import Staff , Flight ,Airport

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Staff)
