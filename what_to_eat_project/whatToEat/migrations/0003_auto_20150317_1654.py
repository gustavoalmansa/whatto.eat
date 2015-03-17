# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('whatToEat', '0002_auto_20150317_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
