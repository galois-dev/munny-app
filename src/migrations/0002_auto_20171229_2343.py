# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-29 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fruitperson',
            name='fruitbool',
            field=models.BooleanField(default=False, help_text='Used to keep track of wether or not the user linked has said fruitful'),
        ),
        migrations.AlterField(
            model_name='user',
            name='MUNID',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
