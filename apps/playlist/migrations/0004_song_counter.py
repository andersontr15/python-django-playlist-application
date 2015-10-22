# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_auto_20151021_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='counter',
            field=models.IntegerField(null=True),
        ),
    ]
