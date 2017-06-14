# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='posting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='links.Link'),
            preserve_default=False,
        ),
    ]
