from django.urls import path

from .views import (
    ParameterDetail,
    ParameterList,
    ParameterCategoryDetail,
    ParameterCategoryList,
    # controller
    WeatherConditionView,
    SetStatusView,
)


urlpatterns = [
    path("parameters/<int:pk>", ParameterDetail.as_view(), name="parameter_detail"),
    path("parameters/", ParameterList.as_view(), name="parameter_list"),
    path(
        "parameters-categories/<int:pk>",
        ParameterCategoryDetail.as_view(),
        name="parameter_category_detail",
    ),
    path(
        "parameters-categories/",
        ParameterCategoryList.as_view(),
        name="parameter_category_list",
    ),
    
    # controller services
    path("weather-condition/", WeatherConditionView.as_view(), name="weather_condition_view"),
    path("set-status/", SetStatusView.as_view(), name="set_status_view"),
]
