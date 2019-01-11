# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-11 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import orm.FileUploader


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0030_auto_20190111_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='calon',
            name='picture2',
            field=models.ImageField(blank=True, default='calon/icon.png', help_text='Upload Fotomu sebagai gambar profile', null=True, upload_to=orm.FileUploader.file_calon),
        ),
    ]