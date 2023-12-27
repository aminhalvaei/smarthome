from rest_framework import serializers

from home.models import Controller


class WeatherRequestSerializer(serializers.Serializer):
    physical_id = serializers.CharField(max_length=12)


class SetStatusSerializer(serializers.Serializer):
    physical_id = serializers.CharField(max_length=12)


class RegisterControllerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("physical_id",)
        model = Controller
