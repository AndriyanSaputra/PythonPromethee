# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-04 04:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0010_auto_20181120_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kesehatan',
            old_name='status',
            new_name='status_kes',
        ),
        migrations.AlterModelTable(
            name='kesehatan',
            table='Kesehatan',
        ),
    ]