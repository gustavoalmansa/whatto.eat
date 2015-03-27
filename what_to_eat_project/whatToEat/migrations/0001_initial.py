# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient_name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredients_In_Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('ingredient', models.ForeignKey(to='whatToEat.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.DecimalField(default=0.0, max_digits=20, decimal_places=2)),
                ('ingredient', models.ForeignKey(to='whatToEat.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('instructions', tinymce.models.HTMLField(default=b' ', max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.CharField(default=b' ', max_length=100)),
                ('shopping', models.ForeignKey(to='whatToEat.Ingredient')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(to='whatToEat.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(to='whatToEat.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inventory',
            name='unit',
            field=models.ForeignKey(to='whatToEat.Unit', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inventory',
            name='user',
            field=models.ForeignKey(to='whatToEat.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredients_in_recipe',
            name='recipe',
            field=models.ForeignKey(to='whatToEat.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredients_in_recipe',
            name='unit',
            field=models.ForeignKey(to='whatToEat.Unit', null=True),
            preserve_default=True,
        ),
    ]
