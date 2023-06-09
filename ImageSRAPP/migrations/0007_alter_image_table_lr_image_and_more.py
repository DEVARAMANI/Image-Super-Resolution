# Generated by Django 4.1.7 on 2023-05-07 18:14

import ImageSRAPP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageSRAPP', '0006_alter_image_table_lr_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_table',
            name='lr_image',
            field=models.ImageField(blank=True, null=True, upload_to=ImageSRAPP.models.file_path),
        ),
        migrations.AlterField(
            model_name='image_table',
            name='sr_image',
            field=models.ImageField(blank=True, null=True, upload_to=ImageSRAPP.models.file_path_sr),
        ),
    ]
