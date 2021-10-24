# Generated by Django 3.2.8 on 2021-10-23 18:04

import cloudinary.models
import datetime
from django.db import migrations, models
import uploader.validators


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0004_alter_photos_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, validators=[uploader.validators.validate_file_size], verbose_name='image'),
        ),
    ]
