from django.db import models
from django.contrib.auth.models import User


class Ingredients(models.Model):
    name = models.CharField(max_length=128, unique=True)
    quantity = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=128,unique = True)
    rating = models.IntegerField(default = 0)
    ingredients = models.ManyToManyField(Ingredients)
    author = models.ForeignKey(User, default = 0)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, unique = True)
    recipes = models.ManyToManyField(Recipe)

    def __unicode__(self):
        return self.name

class Inventory(models.Model):
    user = models.CharField(max_length=30, unique = True)
    ingredients = models.ManyToManyField(Ingredients)

    def __unicode__(self):
        return self.ingredients

class ShoppingList(models.Model):
    user = models.ForeignKey(User)
    shopping = models.ManyToManyField(Ingredients)

    def __unicode__(self):
        return self.shopping

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    inventory = models.OneToOneField(Inventory)

    def __unicode__(self):
        return self.user.username