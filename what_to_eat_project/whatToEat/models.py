from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.ingredient_name


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
    slug = models.SlugField(unique=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(UserProfile)
    category = models.ForeignKey(Category)
    instructions = models.CharField(max_length=5000, default=" ")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class ShoppingList(models.Model):
    user = models.ForeignKey(User)
    quantity = models.CharField(max_length=100, default=" ")
    shopping = models.ForeignKey(Ingredient)

    def __unicode__(self):
        return self.shopping


class Inventory(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length=100, default=" ")
    user = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.ingredient.name


class Ingredients_In_Recipe(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    quantity = models.CharField(max_length=100, default=" ")

    def __unicode__(self):
        return (self.recipe.name, self.ingredient.ingredient_name, self.quantity)