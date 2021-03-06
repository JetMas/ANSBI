# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-07-25 20:36
from __future__ import unicode_literals

import Employment.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('application', models.FileField(upload_to='./applications/', validators=[Employment.validators.validate_file_extension])),
                ('resume', models.FileField(upload_to='./resumes/', validators=[Employment.validators.validate_file_extension])),
                ('transcript', models.FileField(blank=True, upload_to='./transcripts/', validators=[Employment.validators.validate_file_extension], verbose_name='Official College Transcripts, if not then High School Transcripts/Diploma/GED')),
                ('certificate_or_license', models.FileField(blank=True, upload_to='./certificates_or_licenses', validators=[Employment.validators.validate_file_extension], verbose_name='Certificate or License applicable to the position (if applicable)')),
                ('letter_of_interest', models.FileField(blank=True, upload_to='./letter_of_interest/', validators=[Employment.validators.validate_file_extension], verbose_name='Letter of Interest for the position')),
                ('apply_date', models.DateField(verbose_name='apply date')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='./attachments/', validators=[Employment.validators.validate_file_extension])),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employment.Application')),
            ],
        ),
        migrations.CreateModel(
            name='GuideLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('file', models.FileField(upload_to='./guidelines/')),
                ('date', models.DateField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=300)),
                ('job_overview', models.TextField(default='')),
                ('qualifications', models.TextField(default='')),
                ('job_PD', models.FileField(blank=True, upload_to='./job_pd')),
                ('post_date', models.DateField(verbose_name='post date')),
                ('due_date', models.DateField(verbose_name='due date')),
            ],
        ),
    ]
