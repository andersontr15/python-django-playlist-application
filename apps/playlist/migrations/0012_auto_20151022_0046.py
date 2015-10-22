# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0011_auto_20151021_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='song',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(related_name='songs', to='playlist.Song'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='users',
            field=models.ManyToManyField(related_name='users', to='playlist.User'),
        ),
    ]
