from django.urls import path

from .views import (
    ParameterDetail,
    ParameterList,
    ParameterCategoryDetail,
    ParameterCategoryList,
    PreferenceDetail,
    PreferenceList,
    PreferenceChoiceDetail,
    PreferenceChoiceList,
    ConfigDetail,
    ConfigList,
    WeatherConditionDetail,
    WeatherConditionList,
    ParameterValueDetail,
    ParameterValueList,
    ControllerStatusDetail,
    ControllerStatusList,
    StatusValueDetail,
    StatusValueList,
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
    path("preference/<int:pk>", PreferenceDetail.as_view(), name="preference_detail"),
    path("preference/", PreferenceList.as_view(), name="preference_list"),
    path(
        "preference-choice/<int:pk>",
        PreferenceChoiceDetail.as_view(),
        name="preference_choice_detail",
    ),
    path(
        "preference-choice",
        PreferenceChoiceList.as_view(),
        name="preference_choice_list",
    ),
    path("config/<int:pk>", ConfigDetail.as_view(), name="config_detail"),
    path("config/", ConfigList.as_view(), name="config_list"),
    path(
        "weather-condition/<int:pk>",
        WeatherConditionDetail.as_view(),
        name="weather_condition_detail",
    ),
    path(
        "weather-condition/",
        WeatherConditionList.as_view(),
        name="weather_condition_list",
    ),
    path(
        "parameter-value/<int:pk>",
        ParameterValueDetail.as_view(),
        name="parameter_value_detail",
    ),
    path("parameter-value/", ParameterValueList.as_view(), name="parameter_value_list"),
    path(
        "controller-status/<int:pk>",
        ControllerStatusDetail.as_view(),
        name="controller_status_detail",
    ),
    path(
        "controller-status/",
        ControllerStatusList.as_view(),
        name="controller_status_list",
    ),
    path(
        "status-value/<int:pk>", StatusValueDetail.as_view(), name="status_value_detail"
    ),
    path("status-value/", StatusValueList.as_view(), name="status_value_list"),
]
