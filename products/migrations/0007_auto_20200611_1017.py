# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-11 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200611_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='categories',
        ),
    ]