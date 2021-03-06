# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-11 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('singles', 'singles'), ('mixed_cases', 'mixed_cases'), ('merchandise', 'merchandise')], default='singles', max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.Category'),
        ),
    ]
