# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0009_auto_20151021_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(related_name='song', to='playlist.Song'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='user',
            field=models.ManyToManyField(related_name='user', to='playlist.User'),
        ),
    ]
