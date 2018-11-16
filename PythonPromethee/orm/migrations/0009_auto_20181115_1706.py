# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-15 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0008_auto_20181115_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kesehatan',
            name='jasmani',
        ),
        migrations.AddField(
            model_name='kesehatan',
            name='status',
            field=models.CharField(choices=[('SH', 'Sehat'), ('TS', 'Tidak Sehat')], default='SH', max_length=2),
        ),
    ]
