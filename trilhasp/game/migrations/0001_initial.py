# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import game.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameBusAvailability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('available_buses', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameBusBrand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(null=True, upload_to=game.models.get_busbrand_logo_path, blank=True)),
                ('enabled', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameBusModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('efficiency', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('bus_brand', models.ForeignKey(related_name='models', to='game.GameBusBrand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameCoinModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=120)),
                ('value', models.PositiveIntegerField()),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameFinance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveIntegerField()),
                ('coin_model', models.ForeignKey(to='game.GameCoinModel')),
                ('user', models.ForeignKey(related_name='finances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GamePersonalBusFleet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.PositiveIntegerField()),
                ('last_payment', models.DateTimeField()),
                ('bus_model', models.ForeignKey(to='game.GameBusModel')),
                ('user', models.ForeignKey(related_name='bus_fleet', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='gamepersonalbusfleet',
            unique_together=set([('user', 'bus_model')]),
        ),
        migrations.AlterUniqueTogether(
            name='gamefinance',
            unique_together=set([('user', 'coin_model')]),
        ),
        migrations.AddField(
            model_name='gamebusavailability',
            name='bus_model',
            field=models.ForeignKey(to='game.GameBusModel', unique=True),
            preserve_default=True,
        ),
    ]
