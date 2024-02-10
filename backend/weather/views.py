from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from rest_framework import generics, views, status
from rest_framework.response import Response
from datetime import datetime
import requests

from . import configs

from .models import (
    Parameter,
    ParameterCategory,
    Preference,
    PreferenceChoice,
    Config,
    ParameterValue,
    WeatherCondition,
    ControllerStatus,
    StatusValue,
)
from home.models import Controller, Home, Location
from .serializers import (
    ParameterSerializer,
    ParameterCategorySerializer,
    PreferenceSerializer,
    PreferenceChoiceSerializer,
    ConfigSerializer,
    WeatherConditionSerializer,
    ParameterValueSerializer,
    ControllerStatusSerializer,
    StatusValueSerializer,
)


# Create your views here.


class ParameterList(generics.ListCreateAPIView):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class ParameterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class ParameterCategoryList(generics.ListAPIView):
    queryset = ParameterCategory.objects.all()
    serializer_class = ParameterCategorySerializer


class ParameterCategoryDetail(generics.RetrieveAPIView):
    queryset = ParameterCategory.objects.all()
    serializer_class = ParameterCategorySerializer


class PreferenceList(generics.ListCreateAPIView):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer


class PreferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer


class PreferenceChoiceList(generics.ListAPIView):
    queryset = PreferenceChoice.objects.all()
    serializer_class = PreferenceChoiceSerializer


class PreferenceChoiceDetail(generics.RetrieveAPIView):
    queryset = PreferenceChoice.objects.all()
    serializer_class = PreferenceChoiceSerializer


class ConfigList(generics.ListCreateAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class ConfigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class WeatherConditionList(generics.ListCreateAPIView):
    queryset = WeatherCondition.objects.all()
    serializer_class = WeatherConditionSerializer


class WeatherConditionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherCondition.objects.all()
    serializer_class = WeatherConditionSerializer


class ParameterValueList(generics.ListCreateAPIView):
    queryset = ParameterValue.objects.all()
    serializer_class = ParameterValueSerializer


class ParameterValueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParameterValue.objects.all()
    serializer_class = ParameterValueSerializer


class ControllerStatusList(generics.ListCreateAPIView):
    queryset = ControllerStatus.objects.all()
    serializer_class = ControllerStatusSerializer


class ControllerStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ControllerStatus.objects.all()
    serializer_class = ControllerStatusSerializer


class StatusValueList(generics.ListCreateAPIView):
    queryset = StatusValue.objects.all()
    serializer_class = StatusValueSerializer


class StatusValueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StatusValue.objects.all()
    serializer_class = StatusValueSerializer
