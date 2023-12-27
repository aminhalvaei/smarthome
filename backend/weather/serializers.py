from rest_framework import serializers

from .models import Parameter, ParameterCategory


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
