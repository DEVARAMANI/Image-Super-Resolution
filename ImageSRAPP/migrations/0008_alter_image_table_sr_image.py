# Generated by Django 4.1.7 on 2023-05-07 18:16

import ImageSRAPP.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageSRAPP', '0007_alter_image_table_lr_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_table',
            name='sr_image',
            field=models.ImageField(null=True, upload_to=ImageSRAPP.models.file_path_sr),
        ),
    ]