# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-10 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import orm.FileUploader


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0027_pemilih_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemilih',
            name='picture',
            field=models.ImageField(blank=True, default='pemilih/icon.png', help_text='Upload Fotomu sebagai gambar profile', null=True, upload_to=orm.FileUploader.file_profile),
        ),
    ]
