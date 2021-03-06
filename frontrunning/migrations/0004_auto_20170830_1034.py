# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontrunning', '0003_auto_20170829_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='FraudList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_1', models.PositiveIntegerField()),
                ('party_2', models.PositiveIntegerField()),
                ('party_3', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='appleorder',
            name='trade_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='facebookorder',
            name='trade_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='walmartorder',
            name='trade_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
