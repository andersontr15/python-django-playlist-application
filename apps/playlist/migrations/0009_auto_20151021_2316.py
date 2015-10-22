# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0008_auto_20151021_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='song',
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(related_name='song', null=True, to='playlist.Song'),
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ManyToManyField(related_name='user', null=True, to='playlist.User'),
        ),
    ]
