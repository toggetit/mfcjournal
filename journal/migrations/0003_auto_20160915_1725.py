# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_in_out tables'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='actor_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='actor',
            old_name='actor_surname',
            new_name='surname',
        ),
    ]
