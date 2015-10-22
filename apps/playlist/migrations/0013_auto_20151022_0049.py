# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0012_auto_20151022_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='songs',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='users',
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(related_name='song', to='playlist.Song'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ManyToManyField(related_name='user', to='playlist.User'),
        ),
    ]
