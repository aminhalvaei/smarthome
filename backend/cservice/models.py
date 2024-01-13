from django.db import models
from rest_framework_api_key.models import AbstractAPIKey

from home.models import Controller

# Create your models here.


class ControllerAPIKey(AbstractAPIKey):
    controller = models.ForeignKey(
        Controller, on_delete=models.CASCADE, related_name="api_keys"
    )

    class Meta(AbstractAPIKey.Meta):
        verbose_name = "Controller API key"
        verbose_name_plural = "Controllers API keys"
