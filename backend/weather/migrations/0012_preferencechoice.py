# Generated by Django 5.0 on 2023-12-28 16:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0011_alter_weathercondition_controller"),
    ]

    operations = [
        migrations.CreateModel(
            name="PreferenceChoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64)),
                (
                    "impact",
                    models.DecimalField(
                        decimal_places=0,
                        default=0,
                        max_digits=3,
                        validators=[
                            django.core.validators.MinValueValidator,
                            django.core.validators.MaxValueValidator,
                        ],
                    ),
                ),
            ],
            options={
                "verbose_name": "Preference Choice",
                "verbose_name_plural": "Preference Choices",
            },
        ),
    ]
