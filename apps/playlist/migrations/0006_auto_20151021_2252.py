# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0005_auto_20151021_2244'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='playlist',
            table='playlists',
        ),
    ]
