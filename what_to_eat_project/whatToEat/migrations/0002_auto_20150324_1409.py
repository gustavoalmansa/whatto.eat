# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatToEat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.CharField(default=b' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='quantity',
            field=models.CharField(default=b' ', max_length=100),
        ),
    ]
