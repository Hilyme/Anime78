# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-14 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(db_column='name', max_length=32, primary_key=True, serialize=False),
        ),
    ]
