from django.db import models
from django.utils.translation import gettext_lazy as _

from smarthome.settings import AUTH_USER_MODEL as User
from home.models import Controller

# Create your models here.


class ParameterCategory(models.Model):
    title = models.CharField(_("category title"), max_length=64)

    class Meta:
        verbose_name = "Parameter Category"
        verbose_name_plural = "Parameter Categories"

    def __str__(self):
        return self.title


class Parameter(models.Model):
    title = models.CharField(_("parameter title"), max_length=128)
    unit = models.CharField(_("unit of measurment"), max_length=64)
    category = models.ForeignKey(
        ParameterCategory, on_delete=models.SET_NULL, blank=False, null=True
    )
    is_setable = models.BooleanField(blank=True, null=True)
    is_indoor = models.BooleanField(blank=False, null=False)

    class Meta:
        verbose_name = "Parameter"
        verbose_name_plural = "Parameters"

    def __str__(self):
        return self.title


class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias_name = models.CharField(
        _("Preference Name"),
        max_length=128,
        blank=True,
        null=True,
        help_text=_("Optional user defined name for a preference"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Preference"
        verbose_name_plural = "Preferences"

        # A user can not have two preference with same alias names
        unique_together = ("user", "alias_name")

    def __str__(self):
        if self.alias_name is not None:
            return f"{self.alias_name}|{self.user.__str__()}"
        else:
            return f"{self.id}|{self.user.__str__()}"


class Config(models.Model):
    preference = models.ForeignKey(Preference, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        verbose_name = "Config"
        verbose_name_plural = "Configs"

    def __str__(self):
        return self.id


class WeatherCondition(models.Model):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_manual = models.BooleanField(default=False, blank=True, null=False)

    class Meta:
        verbose_name = "Weather Condition"
        verbose_name_plural = "Weather Conditions"

    def __str__(self):
        return self.id


class ParameterValue(models.Model):
    weather_condition = models.ForeignKey(WeatherCondition, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        verbose_name = "ParameterValue"
        verbose_name_plural = "ParameterValues"

    def __str__(self):
        return self.id
