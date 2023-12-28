# Generated by Django 5.0 on 2023-12-28 16:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0014_alter_preferencechoice_title_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="preferencechoice",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="preferencechoice",
            name="impact",
            field=models.DecimalField(
                decimal_places=0,
                default=0,
                max_digits=3,
                unique=True,
                validators=[
                    django.core.validators.MinValueValidator(-50),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]