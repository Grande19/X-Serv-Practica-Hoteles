# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-26 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hoteles', '0004_auto_20160626_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='n_comentarios',
            field=models.IntegerField(default=0),
        ),
    ]