# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sku', models.CharField(max_length=20)),
                ('upc', models.CharField(max_length=13)),
                ('number_part', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Unit_of_measure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('key', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouses_existence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('article', models.ForeignKey(to='inventory.Article')),
                ('warehouse', models.ForeignKey(to='inventory.Warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='unit_of_measure',
            field=models.ForeignKey(to='inventory.Unit_of_measure'),
        ),
    ]
