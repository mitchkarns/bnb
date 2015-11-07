# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temporary_housing', '0004_auto_20151101_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='UProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, db_index=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_org', models.BooleanField(default=False)),
                ('region', models.CharField(max_length=100)),
                ('num_posts', models.IntegerField(default=0)),
                ('contact_requests', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('picture', models.ImageField(upload_to='', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
