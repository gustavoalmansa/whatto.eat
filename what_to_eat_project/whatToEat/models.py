from django.db import models
from django.contrib.auth.models import User


class Ingredients(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ##quantity = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rating = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(Ingredients)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    recipes = models.ManyToManyField(Recipe)

    def __unicode__(self):
        return self.name


class ShoppingList(models.Model):
    user = models.ForeignKey(User)
    shopping = models.ManyToManyField(Ingredients)

    def __unicode__(self):
        return self.shopping


class Inventory(models.Model):
    ingredients = models.ManyToManyField(Ingredients)

    def __unicode__(self):
        return self.ingredients


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    inventory = models.OneToOneField(Inventory)

    def __unicode__(self):
        return self.user.username