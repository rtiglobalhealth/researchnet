# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_studyuser_dob'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudyUser',
            new_name='ParticipantUser',
        ),
    ]
