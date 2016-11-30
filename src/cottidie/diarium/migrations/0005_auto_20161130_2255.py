# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diarium', '0004_auto_20161129_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='notebook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='diarium.Notebook'),
        ),
    ]
