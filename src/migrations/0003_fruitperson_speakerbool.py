# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-29 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20171229_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruitperson',
            name='speakerbool',
            field=models.BooleanField(default=False, help_text='Is this person a speaker?'),
        ),
    ]
