from django.contrib import admin

from .models import Parameter, ParameterCategory

# Register your models here.

admin.site.register(Parameter)
admin.site.register(ParameterCategory)

