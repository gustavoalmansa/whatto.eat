import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'what_to_eat_project.settings')

import django
django.setup()

from whatToEat.models import Ingredient, Recipe, Category, UserProfile
from django.contrib.auth.models import User


def populate():

    for i in xrange(15):
        u = User(username="User "+str(i), password='q')
        u.save()

    print("Users added but not the profiles")
    author_profile = add_profile(User.objects.get(username="User 1"))

    add_ingred("Chicken")
    add_ingred("Egg")
    add_ingred("Honey")
    add_ingred("Soy Sauce")
    add_ingred("Ketchup")
    add_ingred("Milk")
    add_ingred("Rice")
    add_ingred("Mushroom")

    LunchCat = add_cat("Lunch")

    add_recipe(name="Mushroom omelette", rating=4, author=author_profile, category=LunchCat,
               instructions="\n1) Crack the eggs into a mixing bowl \n2) Add a pinch of salt and pepper"
                            "\n3) Beat well with a fork Quarter or roughly chop the mushrooms and add to a small frying"
                            " pan on a high heat with a small knob of butter, a drizzle of olive oil and a pinch of "
                            "salt and pepper"
                            "\n4) Fry and toss around until golden, then turn the heat down to medium "
                            "\n5) Add your eggs and move the pan around to spread them out evenly "
                            "\n6) When the omelette begins to cook and firm up, but still has a little raw egg on top,"
                            " sprinkle over the Cheddar, if using "
                            "\n7) Ease around the edge of the omelette with a spatula, then fold it in half "
                            "\n8) When it starts to turn golden brown underneath, remove the pan from the heat and "
                            "slide the omelette on to a plate")


def add_profile(user):
    up = UserProfile.objects.get_or_create(user=user)[0]
    return up


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


def add_ingred(name):
    i = Ingredient.objects.get_or_create(name=name)[0]
    return i


def add_recipe(name, rating, author, category, instructions):
    r = Recipe.objects.get_or_create(name=name, rating=rating,
                                     author=author, category=category,
                                     instructions=instructions)[0]
    return r

if __name__ == '__main__':
    print "Running population script v0.01"
    populate()
