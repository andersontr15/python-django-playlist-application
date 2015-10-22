# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('counter', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='songs',
            name='counter',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='songs',
            name='users',
        ),
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ManyToManyField(related_name='song', to='playlist.Songs'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ManyToManyField(related_name='user', to='playlist.User'),
        ),
    ]
