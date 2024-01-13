from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin
from rest_framework_api_key.models import APIKey

from .models import ControllerAPIKey

# Register your models here.


class ControllerAPIkeyModelAdmin(APIKeyModelAdmin):
    model = ControllerAPIKey
    list_display = [*APIKeyModelAdmin.list_display, "controller"]
    search_fields = [
        *APIKeyModelAdmin.search_fields,
        "controller",
    ]


admin.site.unregister(APIKey)
admin.site.register(ControllerAPIKey, ControllerAPIkeyModelAdmin)
