# Generated by Django 5.0 on 2023-12-25 09:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0009_alter_parameter_is_setable_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="parametervalue",
            unique_together={("weather_condition", "parameter")},
        ),
        migrations.AlterUniqueTogether(
            name="statusvalue",
            unique_together={("controller_status", "parameter")},
        ),
    ]
