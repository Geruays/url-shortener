# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 15:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0003_auto_20160621_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='alias',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_alias', message='Alias can only contain alphabets, numerals, underscores and hyphens', regex='^[a-zA-Z0-9-_]+$')]),
        ),
    ]
