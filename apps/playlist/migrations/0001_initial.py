# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('title', models.TextField(max_length=20)),
                ('artist', models.TextField(max_length=20)),
                ('counter', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=20)),
                ('last_name', models.TextField(max_length=20)),
                ('email', models.TextField(max_length=20)),
                ('password', models.TextField(max_length=20)),
                ('counter', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='songs',
            name='users',
            field=models.ManyToManyField(related_name='users', to='playlist.User'),
        ),
    ]
