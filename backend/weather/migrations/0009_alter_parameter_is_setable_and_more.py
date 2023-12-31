# Generated by Django 5.0 on 2023-12-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0008_rename_controllerstatus_statusvalue_controller_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parameter",
            name="is_setable",
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name="parameter",
            unique_together={("title", "is_setable", "is_indoor")},
        ),
    ]
