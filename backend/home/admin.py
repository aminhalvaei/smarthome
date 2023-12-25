from django.contrib import admin

from .models import City, Location, Home, Controller, Device

# Register your models here.

class ControllerAdmin(admin.ModelAdmin):
    model = Controller
    list_display = [
        "physical_id",
        "home",
        "alias_name",
        "is_manual",
        "is_active",
        "is_registered",
    ]

admin.site.register(City)
admin.site.register(Location)
admin.site.register(Home)
admin.site.register(Controller, ControllerAdmin)
admin.site.register(Device)


