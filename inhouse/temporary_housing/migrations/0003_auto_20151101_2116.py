# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temporary_housing', '0002_auto_20151030_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('is_active', models.BooleanField(default=True)),
                ('is_org', models.BooleanField(default=False)),
                ('region', models.CharField(max_length=100)),
                ('num_posts', models.IntegerField(default=0)),
                ('contact_requests', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('date_created', models.DateField(verbose_name='date created')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
