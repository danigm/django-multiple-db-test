# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-27 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(default='main test', max_length=200)),
            ],
        ),
    ]
