from atexit import register
from django.contrib import admin
from parkingApp.models import bookings,lots,premises,car,carstate,cartype,businessusers,favourites,status
# Register your models here.

admin.site.register(bookings)
admin.site.register(lots)
admin.site.register(premises)
admin.site.register(car)
admin.site.register(cartype)
admin.site.register(carstate)
admin.site.register(status)
admin.site.register(businessusers)
admin.site.register(favourites)
