# Generated by Django 5.0 on 2023-12-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_alter_controller_registered_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="controller",
            name="registered_at",
            field=models.DateTimeField(
                editable=False, null=True, verbose_name="Registration date"
            ),
        ),
        migrations.AlterField(
            model_name="device",
            name="registered_at",
            field=models.DateTimeField(
                editable=False, null=True, verbose_name="Registration date"
            ),
        ),
    ]
