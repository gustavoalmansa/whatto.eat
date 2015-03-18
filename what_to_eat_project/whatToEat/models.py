from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


class Ingredients(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rating = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(Ingredients)
    author = models.ForeignKey(UserProfile)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name


class ShoppingList(models.Model):
    user = models.ForeignKey(User)
    shopping = models.ManyToManyField(Ingredients)

    def __unicode__(self):
        return self.shopping


class Inventory(models.Model):
    ingredients = models.ForeignKey(Ingredients)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    user = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.ingredients