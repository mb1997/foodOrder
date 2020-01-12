# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-01-09 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('img', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
