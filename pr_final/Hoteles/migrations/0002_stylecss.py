# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-22 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hoteles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyleCSS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.TextField(blank=True)),
                ('banner', models.TextField(blank=True)),
                ('login', models.TextField(blank=True)),
                ('menu', models.TextField(blank=True)),
                ('pie', models.TextField(blank=True)),
            ],
        ),
    ]