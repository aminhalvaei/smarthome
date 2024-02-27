from rest_framework import serializers

from .models import City, Location, InsulationLevel, Home, Controller, Device


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "country",
            "province",
        )
        model = City


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "city",
            "latitude",
            "longitude",
        )
        model = Location
        
class InsulationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "impact",
        )
        model = InsulationLevel


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "alias_name",
            "user",
            "location",
        )
        model = Home


class ControllerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "physical_id",
            "home",
            "alias_name",
            "is_manual",
            "is_active",
            "is_registered",
            "created_at",
            "registered_at",
        )
        model = Controller


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "physical_id",
            "controller",
            "alias_name",
        )
        model = Device
