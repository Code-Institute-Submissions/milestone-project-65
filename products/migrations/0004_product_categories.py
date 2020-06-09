# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-09 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_delete_cases'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.CharField(choices=[('singles', 'singles'), ('mixed_cases', 'mixed_cases'), ('merchandise', 'merchandise')], default='singles', max_length=120),
        ),
    ]
