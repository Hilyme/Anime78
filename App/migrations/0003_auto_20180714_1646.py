# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-14 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20180714_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='u_email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='u_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='pwd',
            new_name='u_pwd',
        ),
    ]