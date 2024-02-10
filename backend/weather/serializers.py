from rest_framework import serializers

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


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "unit",
            "category",
            "is_setable",
            "is_indoor",
        )

        model = Parameter


class ParameterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
        )

        model = ParameterCategory


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "user",
            "alias_name",
            "created_at",
            "updated_at",
        )

        model = Preference


class PreferenceChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "impact",
        )

        model = PreferenceChoice


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "preference",
            "parameter",
            "value",
        )

        model = Config


class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "controller",
            "created_at",
            "updated_at",
        )

        model = WeatherCondition


class ParameterValueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "weather_condition",
            "parameter",
            "value",
        )

        model = ParameterValue


class ControllerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "controller",
            "is_pending",
            "created_at",
            "updated_at",
        )

        model = ControllerStatus


class StatusValueSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "controller_status",
            "parameter",
            "value",
        )

        model = StatusValue
