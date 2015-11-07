# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temporary_housing', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Organizer',
        ),
        migrations.AddField(
            model_name='user',
            name='can_invite',
            field=models.IntegerField(default=0),
        ),
    ]
