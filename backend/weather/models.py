from django.db import models
from django.utils.translation import gettext_lazy as _

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
