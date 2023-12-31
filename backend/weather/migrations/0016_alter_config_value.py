# Generated by Django 5.0 on 2023-12-28 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0015_alter_preferencechoice_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="config",
            name="value",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="config",
                to="weather.preferencechoice",
            ),
        ),
    ]
