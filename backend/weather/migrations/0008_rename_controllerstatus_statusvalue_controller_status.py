# Generated by Django 5.0 on 2023-12-25 08:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("weather", "0007_alter_parametervalue_options_controllerstatus_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="statusvalue",
            old_name="controllerstatus",
            new_name="controller_status",
        ),
    ]