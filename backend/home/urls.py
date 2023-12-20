from django.urls import path

from .views import (
    CityList,
    CityDetail,
    LocationList,
    LocationDetail,
    HomeList,
    HomeDetail,
    ControllerList,
    ControllerDetail,
    DeviceList,
    DeviceDetail,
)

urlpatterns = [
    path("cities/", CityList.as_view(), name="city-list"),
    path("cities/<int:pk>/", CityDetail.as_view(), name="city-detail"),
    path("locations/", LocationList.as_view(), name="location-list"),
    path("locations/<int:pk>/", LocationDetail.as_view(), name="location-detail"),
    path("homes/", HomeList.as_view(), name="home-list"),
    path("homes/<int:pk>", HomeDetail.as_view(), name="home-detail"),
    path("controllers/", ControllerList.as_view(), name="controller-list"),
    path("controllers/<int:pk>", ControllerDetail.as_view(), name="controller-detail"),
    path("devices/", DeviceList.as_view(), name="device-list"),
    path("devices/<int:pk>", DeviceDetail.as_view(), name="device-detail"),
]
