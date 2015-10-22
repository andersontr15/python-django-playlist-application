# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0013_auto_20151022_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='song',
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(related_name='songs', to='playlist.Song'),
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
