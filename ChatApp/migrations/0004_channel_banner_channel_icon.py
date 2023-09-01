# Generated by Django 4.2.4 on 2023-09-01 06:16

import ChatApp.models
import ChatApp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ChatApp", "0003_category_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="channel",
            name="banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=ChatApp.models.server_banner_upload_path,
                validators=[ChatApp.validators.validate_image_file_extension],
            ),
        ),
        migrations.AddField(
            model_name="channel",
            name="icon",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=ChatApp.models.server_icon_upload_path,
                validators=[
                    ChatApp.validators.validate_icon_image_size,
                    ChatApp.validators.validate_image_file_extension,
                ],
            ),
        ),
    ]