# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whatToEat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shopping', models.ManyToManyField(to='whatToEat.Ingredients')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='recipes',
            field=models.ManyToManyField(to='whatToEat.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredients',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inventory',
            name='ingredients',
            field=models.ManyToManyField(to='whatToEat.Ingredients'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(default=b'WhatToEat staff', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='whatToEat.Ingredients'),
            preserve_default=True,
        ),
    ]
