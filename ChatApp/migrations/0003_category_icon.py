# Generated by Django 4.2.4 on 2023-08-18 06:55

import ChatApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ChatApp", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="icon",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=ChatApp.models.category_icon_upload_path,
            ),
        ),
    ]
