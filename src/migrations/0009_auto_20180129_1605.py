# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-29 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_auto_20180129_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitvote',
            name='InitDate',
            field=models.DateTimeField(default='2018-01-31 12:00', help_text='Date and time of creation'),
        ),
    ]
