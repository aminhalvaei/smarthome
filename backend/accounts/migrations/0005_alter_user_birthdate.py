# Generated by Django 5.0 on 2023-12-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthdate",
            field=models.DateField(blank=True, null=True, verbose_name="Birthday"),
        ),
    ]