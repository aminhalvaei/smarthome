from django.contrib import admin

from .models import (
    Parameter,
    ParameterCategory,
    Preference,
    PreferenceChoice,
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


class PreferenceAdmin(admin.ModelAdmin):
    model = Preference
    list_display = [
        "user",
        "alias_name",
    ]


class PreferenceChoiceAdmin(admin.ModelAdmin):
    model = PreferenceChoice
    list_display = ["title", "impact"]
    
class ConfigAdmin(admin.ModelAdmin):
    model = Config
    list_display = [
        "preference",
        "parameter",
        "value",
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


admin.site.register(Parameter, ParameterAdmin)
admin.site.register(ParameterCategory)
admin.site.register(Preference, PreferenceAdmin)
admin.site.register(PreferenceChoice, PreferenceChoiceAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(WeatherCondition)
admin.site.register(ParameterValue, ParameterValueAdmin)
admin.site.register(ControllerStatus, ControllerStatusAdmin)
admin.site.register(StatusValue, StatusValueAdmin)
