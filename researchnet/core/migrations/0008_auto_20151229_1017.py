# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151228_1528'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ParticipantUser',
            new_name='Participant',
        ),
    ]
