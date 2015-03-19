from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=128, unique=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(UserProfile)
    category = models.ForeignKey(Category)
    instructions = models.CharField(max_length = 5000, default = " ")

    def __unicode__(self):
        return self.name


class ShoppingList(models.Model):
    user = models.ForeignKey(User)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    shopping = models.ForeignKey(Ingredient)

    def __unicode__(self):
        return self.shopping


class Inventory(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    user = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.ingredient

class Ingredients_In_Recipe(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    def __unicode__(self):
        return self.recipe.name