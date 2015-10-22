# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0004_song_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='counter',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
