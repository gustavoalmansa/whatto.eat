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
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    rating = models.IntegerField()
    author = models.ForeignKey(UserProfile)
    category = models.ForeignKey(Category)
    instructions = models.CharField(max_length=5000, default=" ")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.rating = self.likes-self.dislikes
        super(Recipe, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.name


class ShoppingList(models.Model):
    user = models.ForeignKey(User)
    quantity = models.CharField(max_length=100, default=" ")
    shopping = models.ForeignKey(Ingredient)

    def __unicode__(self):
        return self.shopping


class Unit(models.Model):
    unit_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.unit_name


class Inventory(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    user = models.ForeignKey(UserProfile)
    unit = models.ForeignKey(Unit, null=True)

    def __unicode__(self):
        return self.ingredient.name


class Ingredients_In_Recipe(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    unit = models.ForeignKey(Unit, null=True)

    def __unicode__(self):

        return str(self.quantity)+" " + str(self.unit) +" " +self.ingredient.ingredient_name+" "+self.recipe.name