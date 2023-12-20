from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User

# Create your models here.


class City(models.Model):
    name = models.CharField(_("City Name"), max_length=128, blank=False, null=False)
    country = models.CharField(
        _("Country Name"), max_length=64, blank=False, null=False
    )
    province = models.CharField(
        _("Province Name"), max_length=128, blank=False, null=False
    )

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=False, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=False, null=False
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=False, null=False
    )

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"


class Home(models.Model):
    alias_name = models.CharField(
        _("Home name"),
        max_length=128,
        blank=True,
        null=True,
        help_text=_("Optional user defined name for a home"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, blank=False, null=True
    )

    class Meta:
        verbose_name = _("Home")
        verbose_name_plural = _("Homes")

    def __str__(self):
        return f"Home:{self.id}"


class Controller(models.Model):
    physical_id = models.CharField(
        _("Physical id of Controller"),
        max_length=12,
        unique=True,
        db_index=True,
        blank=False,
        null=False,
    )
    home = models.ForeignKey(Home, on_delete=models.CASCADE, blank=False, null=False)
    alias_name = models.CharField(
        _("Controller name"),
        max_length=128,
        blank=True,
        null=True,
        help_text=_("Optional user defined name for a controller"),
    )
    is_active = models.BooleanField(_("Activation status"), default=False, null=False)
    is_registered = models.BooleanField(
        _("Registration status"), default=False, null=False
    )
    created_at = models.DateTimeField(_("Creation date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Last update"), auto_now=True)
    registered_at = models.DateTimeField(
        _("Registration date"), editable=False, null=True
    )

    class Meta:
        verbose_name = _("Controller")
        verbose_name_plural = _("Controllers")

    def __str__(self):
        return f"{self.physical_id}:{self.alias_name}"


class Device(models.Model):
    physical_id =  models.CharField(
            _("Physical id of Device"),
            max_length=12,
            unique=True,
            db_index=True,
            blank=False,
            null=False,
    )
    controller = models.ForeignKey(
        Controller, on_delete=models.CASCADE, blank=False, null=False
    )
    alias_name = models.CharField(
        _("Device name"),
        max_length=128,
        blank=True,
        null=True,
        help_text=_("Optional user defined name for a controller"),
    )
    is_active = models.BooleanField(_("Activation status"), default=False, null=False)
    is_registered = models.BooleanField(
        _("Registration status"), default=False, null=False
    )
    created_at = models.DateTimeField(_("Creation date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Last update"), auto_now=True)
    registered_at = models.DateTimeField(
        _("Registration date"), editable=False, null=True
    )

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self):
        return f"{self.physical_id}:{self.alias_name}"
