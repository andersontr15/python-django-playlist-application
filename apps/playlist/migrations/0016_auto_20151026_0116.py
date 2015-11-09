# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0015_auto_20151022_0114'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='playlist',
            table='playlists',
        ),
        migrations.AlterModelTable(
            name='song',
            table='songs',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
