# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField(default=-1)),
                ('plugin_id', models.IntegerField(default=-1)),
                ('token', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]
