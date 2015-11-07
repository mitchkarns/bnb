# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('hashword_with_salt', models.CharField(max_length=120)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('region', models.CharField(max_length=100)),
                ('num_posts', models.IntegerField(default=0)),
                ('contact_requests', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to='', blank=True)),
                ('date_created', models.DateField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('hashword_with_salt', models.CharField(max_length=120)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('region', models.CharField(max_length=100)),
                ('num_posts', models.IntegerField(default=0)),
                ('contact_requests', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to='', blank=True)),
                ('date_created', models.DateField(verbose_name='date created')),
            ],
        ),
    ]
