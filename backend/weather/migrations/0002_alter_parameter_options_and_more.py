# Generated by Django 5.0 on 2023-12-15 14:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="parameter",
            options={"verbose_name": "Parameter", "verbose_name_plural": "Parameters"},
        ),
        migrations.AlterModelOptions(
            name="parametercategory",
            options={
                "verbose_name": "Parameter Category",
                "verbose_name_plural": "Parameter Categories",
            },
        ),
    ]