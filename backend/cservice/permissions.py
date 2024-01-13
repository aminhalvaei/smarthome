from rest_framework_api_key.permissions import BaseHasAPIKey

from .models import ControllerAPIKey


class HasControllerAPIKey(BaseHasAPIKey):
    model = ControllerAPIKey
