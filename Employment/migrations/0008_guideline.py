# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-07-18 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employment', '0007_auto_20170718_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('file', models.FileField(upload_to='./guidelines/')),
            ],
        ),
    ]