from django.urls import path

from .views import (
    ParameterDetail,
    ParameterList,
    ParameterCategoryDetail,
    ParameterCategoryList,
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
]
