from django.contrib import admin

from .models import City, Location, Home, Controller, Device

# Register your models here.

admin.site.register(City)
admin.site.register(Location)
admin.site.register(Home)
admin.site.register(Controller)
admin.site.register(Device)


