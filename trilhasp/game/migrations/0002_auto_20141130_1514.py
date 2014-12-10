# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamepersonalbusfleet',
            name='last_payment',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
