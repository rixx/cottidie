# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 17:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diarium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diaria', to=settings.AUTH_USER_MODEL),
        ),
    ]
