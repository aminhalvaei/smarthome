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
    ParameterValue,
    WeatherCondition,
    ControllerStatus,
    StatusValue,
)
from home.models import Controller, Home, Location
from .serializers import ParameterSerializer, ParameterCategorySerializer


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
