# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0006_auto_20151021_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='song',
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ForeignKey(related_name='song', to='playlist.Song', null=True),
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(related_name='user', to='playlist.User', null=True),
        ),
    ]
