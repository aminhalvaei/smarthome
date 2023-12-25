from django.contrib import admin

from .models import (
    Parameter,
    ParameterCategory,
    Preference,
    Config,
    WeatherCondition,
    ParameterValue,
    ControllerStatus,
    StatusValue,
)

# Register your models here.

class ParameterAdmin(admin.ModelAdmin):
    model = Parameter
    list_display = [
        "title",
        "unit",
        "category",
        "is_setable",
        "is_indoor",
    ]
    
class ParameterValueAdmin(admin.ModelAdmin):
    model = ParameterValue
    list_display = [
        "weather_condition",
        "parameter",
        "value",
    ]
    
class ControllerStatusAdmin(admin.ModelAdmin):
    model = ControllerStatus
    list_display = [
        "controller",
        "is_pending",
    ]
    
class StatusValueAdmin(admin.ModelAdmin):
    model = StatusValue
    list_display = [
        "controller_status",
        "parameter",
        "value",
    ]

admin.site.register(Parameter,ParameterAdmin)
admin.site.register(ParameterCategory)
admin.site.register(Preference)
admin.site.register(Config)
admin.site.register(WeatherCondition)
admin.site.register(ParameterValue, ParameterValueAdmin)
admin.site.register(ControllerStatus, ControllerStatusAdmin)
admin.site.register(StatusValue, StatusValueAdmin)
