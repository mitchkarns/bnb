# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temporary_housing', '0003_auto_20151101_2116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='UserProfile',
        ),
    ]
