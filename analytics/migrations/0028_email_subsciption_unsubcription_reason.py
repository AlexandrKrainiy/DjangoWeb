# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0027_remove_email_subsciption_unsubcription_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='email_subsciption',
            name='unsubcription_reason',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]