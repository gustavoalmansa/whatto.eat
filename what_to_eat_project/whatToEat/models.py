from django.db import models


class Ingredients(models.Model):

    name = models.CharField(max_length=128, unique=True)
    quantity = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name