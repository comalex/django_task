# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_day',
            field=models.DateField(blank=True, null=True, verbose_name='Birth day'),
        ),
    ]
