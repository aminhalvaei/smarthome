from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User

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
    city_id = models.ForeignKey(City, on_delete=models.SET_NULL, blank=False, null=True)
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
    User_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    loc_id = models.ForeignKey(
        Location, on_delete=models.SET_NULL, blank=False, null=True
    )

    class Meta:
        verbose_name = _("Home")
        verbose_name_plural = _("Homes")

    def __str__(self):
        return f"Home:{self.id}"
