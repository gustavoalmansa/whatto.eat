import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'what_to_eat_project.settings')

import django
django.setup()

from whatToEat.models import Ingredients

def populate():

    add_ingred("Chicken")
    add_ingred("Egg")
    add_ingred("Honey")
    add_ingred("Soy Sauce")
    add_ingred("Ketchup")

    ##add_recipe("Fried Egg",
    ##           5,
    ##           ingredients = ["Egg"])




def add_ingred(name):
    i = Ingredients.objects.get_or_create(name=name)[0]
    return i

def add_recipe(name, rating, ingredients):
    recipe, created = Recipe.objects.get_or_create(name=name)
    recipe.rating = 5
    ##recipe.ingredients.add(*Ingredients.objects.filter(name__in=[ingredients]))

if __name__ == '__main__':
    print "Running population script v0.01"
    populate()
