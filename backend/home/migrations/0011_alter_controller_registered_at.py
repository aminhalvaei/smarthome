# Generated by Django 5.0 on 2023-12-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0010_alter_controller_home"),
    ]

    operations = [
        migrations.AlterField(
            model_name="controller",
            name="registered_at",
            field=models.DateTimeField(null=True, verbose_name="Registration date"),
        ),
    ]
