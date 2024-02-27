from django.contrib import admin

from .models import City, Location, InsulationLevel, Home, Controller, Device

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = [
        "id",
        "name",
        "country",
        "province",
    ]

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = [
        "id",
        "city",
        "latitude",
        "longitude",
    ]

class InsulationLevelAdmin(admin.ModelAdmin):
    model = InsulationLevel
    list_display = [
        "id",
        "title",
        "impact",
    ]

class HomeAdmin(admin.ModelAdmin):
    model = Home
    list_display = [
        "id",
        "alias_name",
        "user",
        "location",
        "insulation_level",
    ]

class ControllerAdmin(admin.ModelAdmin):
    model = Controller
    list_display = [
        "id",
        "physical_id",
        "home",
        "alias_name",
        "is_manual",
        "is_active",
        "is_registered",
        "is_register_pending",
    ]
    


admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(InsulationLevel, InsulationLevelAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Controller, ControllerAdmin)
admin.site.register(Device)
