# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 22:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0008_auto_20170613_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='link',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]