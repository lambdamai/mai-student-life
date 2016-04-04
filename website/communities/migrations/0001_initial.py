# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=250)),
                ('description', models.TextField(default='', max_length=500)),
                ('vk_link', models.CharField(default='', max_length=100)),
                ('contacts', models.TextField(default='', max_length=300)),
                ('community_type', models.CharField(choices=[('reg', 'Regular'), ('hon', 'Honorary')], default='reg', max_length=3)),
            ],
        ),
    ]