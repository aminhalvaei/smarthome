from django.urls import path

from .views import WeatherConditionView, SetStatusView, RegisterControllerView


urlpatterns = [
    path(
        "weather-condition/",
        WeatherConditionView.as_view(),
        name="weather_condition_view",
    ),
    path("set-status/", SetStatusView.as_view(), name="set_status_view"),
    path(
        "register-controller/",
        RegisterControllerView.as_view(),
        name="register_controller_view",
    ),
]
