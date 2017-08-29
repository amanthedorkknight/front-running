# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppleCustomerOrder',
            fields=[
                ('trade_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.PositiveIntegerField()),
                ('trade_type', models.CharField(max_length=200)),
                ('security_type', models.CharField(max_length=200)),
                ('security_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppleFirmOrder',
            fields=[
                ('trade_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.PositiveIntegerField()),
                ('trade_type', models.CharField(max_length=200)),
                ('security_type', models.CharField(max_length=200)),
                ('security_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookCustomerOrder',
            fields=[
                ('trade_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.PositiveIntegerField()),
                ('trade_type', models.CharField(max_length=200)),
                ('security_type', models.CharField(max_length=200)),
                ('security_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookFirmOrder',
            fields=[
                ('trade_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.PositiveIntegerField()),
                ('trade_type', models.CharField(max_length=200)),
                ('security_type', models.CharField(max_length=200)),
                ('security_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WallmartCustomerOrder',
            fields=[
                ('trade_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.PositiveIntegerField()),
                ('trade_type', models.CharField(max_length=200)),
                ('security_type', models.CharField(max_length=200)),
                ('security_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WalmartFirmOrder',
            fields=[
                ('trade_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.PositiveIntegerField()),
                ('trade_type', models.CharField(max_length=200)),
                ('security_type', models.CharField(max_length=200)),
                ('security_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]