import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'what_to_eat_project.settings')

import django
django.setup()

from whatToEat.models import Ingredients

def populate():

    add_ingred("Eggs", 4)
    add_ingred()




def add_ingred(name, quantity):
    i = Ingredients.objects.get_or_create(name=name, quantity=quantity)
    return i


if __name__ == '__main__':
    print "Running population script v0.01"
    populate()
