from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from rest_framework import generics, views, status

from .models import (
    Parameter,
    ParameterCategory,
    ParameterValue,
    WeatherCondition,
    ControllerStatus,
    StatusValue,
)
from home.models import Controller
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


# controller views


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
            parameters = ParameterValue.objects.filter(
                weather_condition__controller__physical_id=physical_id
            )
            # TODO check if the stored data is expired and if it is make an api call to get and update data

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
        return JsonResponse(response_data)


class SetStatusView(views.APIView): # TODO fix the bug here
    def post(self, request, *args, **kwargs):
        serializer = SetStatusSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        physical_id = serializer.validated_data["physical_id"]

        try:
            controller_status = ControllerStatus.objects.get(
                controller__physical_id=physical_id
            )
            if controller_status.is_pending is True:
                controller_status.is_pending = False
                controller_status.save()
                return JsonResponse({"message": "Not pending anymore"}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error": "It already is not pending"}, status=status.HTTP_400_BAD_REQUEST)

        except ControllerStatus.DoesNotExist:
            return JsonResponse({"error": "Object not found."}, status=status.HTTP_404_NOT_FOUND)
