from django.db import models
from django.contrib.auth.models import User


class Ingredients(models.Model):
    name = models.CharField(max_length=128, unique=True)
    quantity = models.IntegerField(default=0)
    recipes = ManyToManyField(Recipe)
    inventories = ManyToManyField(Inventory)
    shoppingLists = ManyToManyField(ShoppingList)

    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=128,unique = True)
    rating = models.IntegerField(max_value = 5,default = 0)
    categories = models.ManyToManyField(Category)
    ingredients = models.ManyToManyField(Ingredients)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, unique = True)
    recipes = models.ManyToManyField(Recipe)
    ingredients = models.ManyToManyField(Ingredients)

    def __unicode__(self):
        return self.name

class Inventory(models.Model):
    user = models.CharField(max_length=30, unique = True)
    ingredients = ManyToManyField(Ingredients)

class ShoppingList(models.Model):
    user = models.ForeignKey(User)
    shopping = models.ManyToManyField(Ingredients)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    inventory = OneToOneField(Inventory)

    def __unicode__(spictureelf):
        return self.user.username