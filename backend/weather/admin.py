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

admin.site.register(Parameter)
admin.site.register(ParameterCategory)
admin.site.register(Preference)
admin.site.register(Config)
admin.site.register(WeatherCondition)
admin.site.register(ParameterValue)
admin.site.register(ControllerStatus)
admin.site.register(StatusValue)
