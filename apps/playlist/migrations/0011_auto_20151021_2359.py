# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0010_auto_20151021_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='updated_at',
        ),
    ]
