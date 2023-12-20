from django.shortcuts import render
from rest_framework import generics

from .models import City, Location, Home, Controller, Device
from .serializers import (
    CitySerializer,
    LocationSerializer,
    HomeSerializer,
    ControllerSerializer,
    DeviceSerializer,
)

# Create your views here.

#### City, Location, Home ####
# Full control over these three models front-end


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


#### Controller, Device ####
# controller and device are only created by their request
# from local server and front-end can not create one
# so ListAPIView is used instead of ListCreateAPIView

# controller and device can not be deleted and it only can be deactivated by is_active field


class ControllerList(generics.ListAPIView):
    queryset = Controller.objects.all()
    serializer_class = ControllerSerializer


class ControllerDetail(generics.RetrieveUpdateAPIView):
    queryset = Controller.objects.all()
    serializer_class = ControllerSerializer


class DeviceList(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveUpdateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
