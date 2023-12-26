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
from .serializers import (
    ParameterSerializer,
    ParameterCategorySerializer,
    # controller
    WeatherRequestSerializer,
    SetStatusSerializer,
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


# Controller views


# Routine 1
class WeatherConditionView(views.APIView):
    def get(self, request, *args, **kwargs):
        serializer = WeatherRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        physical_id = serializer.validated_data["physical_id"]
        controller = get_object_or_404(Controller, physical_id=physical_id)

        if controller.is_manual is True:
            parameters = StatusValue.objects.filter(
                controller_status__controller__physical_id=physical_id
            )
        else:
            latest_update = controller.weather_condition.updated_at
            if self.is_weather_valid(latest_update):
                parameters = ParameterValue.objects.filter(
                    weather_condition__controller__physical_id=physical_id
                )
            else:  # here we need to get new data from api
                self.update_weather_data(physical_id)

        # Prepare the JSON response
        response_data = {
            "is_manual": controller.is_manual,
            "parameters": [
                {
                    "title": parameter.parameter.title,
                    "value": parameter.value,
                }
                for parameter in parameters
            ],
        }

        # Return the data as JSON using JsonResponse
        return Response(response_data, status=status.HTTP_200_OK)

    def is_weather_valid(updated_at):
        deadline = updated_at + configs.WEATHER_VALID_DURATION
        current = datetime.now()
        return deadline >= current

    def update_weather_data(self, physical_id):
        location = Location.objects.get(home__controller__physical_id=physical_id)
        raw_new_data = self.make_api_request(location)
        processed_new_data = self.process_api_response(raw_new_data)
        # TODO continue from here you need to implement two functions process_api_response and insert_parameters

    def make_api_request(location):
        latitude, longitude = location.latitude, location.longitude
        unit = configs.UNITS_OF_MEASUREMENT
        api_key = configs.WEATHER_API_KEYS[0]
        constant_url = configs.CONSTANT_URL

        api_url = f"{constant_url}?lat={latitude}&lon={longitude}&appid={api_key}&units={unit}"

        response = requests.get(api_url)

        return response.json()

    def process_api_response(raw_new_data):
        pass
        # TODO

    def insert_parameters(processed_new_data):
        pass
        # TODO


# Routine 3
class SetStatusView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = SetStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        physical_id = serializer.validated_data["physical_id"]

        try:
            controller_status = ControllerStatus.objects.get(
                controller__physical_id=physical_id
            )
            if controller_status.is_pending is True:
                controller_status.is_pending = False
                controller_status.save()
                return Response(
                    {"message": "Pending flag successfully changed to false"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Pending is already false"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except ControllerStatus.DoesNotExist:
            return Response(
                {"error": "Object not found."}, status=status.HTTP_404_NOT_FOUND
            )
