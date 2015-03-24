import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'what_to_eat_project.settings')

import django
django.setup()

from whatToEat.models import Ingredient, Recipe, Category, UserProfile, Inventory, Ingredients_In_Recipe
from django.contrib.auth.models import User


def populate():

    for i in xrange(15):
        u = User(username="User "+str(i), password='q')
        u.save()

    author_profile = add_profile(User.objects.get(username="User 1"))
    print("Users added")

    chicken_breast = add_ingred("Chicken Breast")
    egg_ingredient = add_ingred("Eggs")
    honey = add_ingred("Honey")
    soy_sauce = add_ingred("Soy Sauce")
    ketchup = add_ingred("Ketchup")
    milk = add_ingred("Milk")
    rice = add_ingred("Rice")
    mushroom = add_ingred("Mushroom")
    salt = add_ingred("Salt")
    pepper = add_ingred("Pepper")
    butter = add_ingred("Butter")
    olive_oil = add_ingred("Olive oil")
    cheddar_cheese = add_ingred("Cheddar Cheese")
    white_bread = add_ingred("White Bread")
    four_cheese_sauce = add_ingred("Four Cheese Sauce")
    spring_onion = add_ingred("Spring Onions")
    sliced_ham = add_ingred("Sliced Ham")
    lemon = add_ingred("Lemon")
    tomato_puree = add_ingred("Tomato Puree")
    dijon = add_ingred("Dijon Mustard")
    chicken_drumstick = add_ingred("Chicken Drumsticks")

    print("Ingredients added")

    add_cat("All Recipes")
    breakfast =add_cat("Breakfast")
    lunch = add_cat("Lunch")
    snack  = add_cat("Snacks")
    dinner  = add_cat("Dinner")
    dessert = add_cat("Dessert")
    print("Catagories added")

    mushroomOmlette = add_recipe(name="Mushroom omelette", rating=4, author=author_profile, category=lunch,
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
    print("Recipe added")

    relate_ingred_to_recipe(egg_ingredient, mushroomOmlette, "2 large")
    relate_ingred_to_recipe(salt, mushroomOmlette, "A pinch of")
    relate_ingred_to_recipe(pepper, mushroomOmlette, "A pinch of")
    relate_ingred_to_recipe(butter, mushroomOmlette, "A knob of")
    relate_ingred_to_recipe(olive_oil, mushroomOmlette, "A splash of")
    relate_ingred_to_recipe(cheddar_cheese, mushroomOmlette, "A handful of")
    relate_ingred_to_recipe(mushroom, mushroomOmlette, "3 large")

    add_ingredient_to_inventory(author_profile, 2.0, chicken_breast)
    add_ingredient_to_inventory(author_profile, 3.0, egg_ingredient)
    print("Ingredients added to inventory")

    cheeseOnionRarebit = add_recipe(name="Quick Cheese and Onion Rarebit",
                                    rating=3, author=author_profile,
                                    category=snack,
                                    instructions = "1)Toast the bread in a toaster. Meanwhile, mix the cheese sauce, onions and a grind of pepper together in a small bowl.\n2)Transfer the toast to a non-stick grill rack and drape the ham over each slice. Next, spoon the cheese sauce onto the ham and spread it around with the back of the spoon. Scatter the grated cheese over the sauce, then pop the rarebit under a hot grill until the cheese turns bubbly and golden. Cut each slice in half and serve while still hot.")


    relateIngredientDictToRecipe({white_bread:"4 slices of",
                                  four_cheese_sauce:"350g tub of",
                                  spring_onion:"3, finely sliced",
                                  sliced_ham:"100g",
                                  cheddar_cheese:"50g"},
                                cheeseOnionRarebit)

    honeyGlazedChicken = add_recipe(name = "Honey Glazed Chicken",
                                    rating=5,
                                    author = author_profile,
                                    category=dinner,
                                    instructions = "1)Put 2 chicken breasts, skin side up in a small baking dish and season.\n2)Squeeze the lemon into a bowl and stir in the honey and soy sauce. Spoon the mixture over the chicken, then tuck the squeezed-out half of lemon between the pieces (this will moisten and add flavour to the chicken).\n3)Roast the chicken breasts in a baking dish, uncovered, for 30-35 minutes in a preheated oven (190C/gas 5/fan oven 170C). Cook until done and richly glazed, basting with the juices at least twice. To check if they are done, prod the chicken with your finger - if it's still a bit soft, give it a bit longer.\n4)Serve with salad and potatoes roasted with herbs and garlic.")


    relateIngredientDictToRecipe({chicken_breast:"2",
                                  lemon:"half of a",
                                  honey:"One Tablespoon",
                                  soy_sauce:"One Tablespoon"},
                                 honeyGlazedChicken)

    stickyChickenDrumstick = add_recipe("Sticky Chicken Drumstick",
                                        rating = 4, author = author_profile,
                                        category=dinner,
                                        instructions="1)Make 3 slashes on each of the drumsticks. Mix together the soy, honey, oil, tomato puree and mustard. Pour this mixture over the chicken and coat thoroughly. Leave to marinate for 30 mins at room temperature or overnight in the fridge. Heat oven to 200C/fan 180C/gas 6.\n2)Tip the chicken into a shallow roasting tray and cook for 35 mins, turning occasionally, until the chicken is tender and glistening with the marinade.")

    relateIngredientDictToRecipe({chicken_drumstick:"Eight",
                                  soy_sauce:"Two Tablespoons",
                                  honey:"One Tablespoon",
                                  olive_oil:"One Tablespoon",
                                  tomato_puree: "One Tablespoon",
                                  dijon:"One Tablespoon"},
                                 stickyChickenDrumstick)

    print ("Recipes added, and ingredients related")

def add_profile(user):
    up = UserProfile.objects.get_or_create(user=user)[0]
    return up


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


def add_ingred(name):
    i = Ingredient.objects.get_or_create(name=name)[0]
    return i

def relateIngredientDictToRecipe(ingredientDict, recipe):
    for ingredient in ingredientDict:
        relate_ingred_to_recipe(ingredient, recipe, ingredientDict[ingredient])

def add_recipe(name, rating, author, category, instructions):
    r = Recipe.objects.get_or_create(name=name, rating=rating,
                                     author=author, category=category,
                                     instructions=instructions)[0]
    return r


def add_ingredient_to_inventory(user_profile, quantity, ingredient):
    i = Inventory.objects.get_or_create(
        user=user_profile,
        quantity=quantity,
        ingredient=ingredient)[0]
    return i


def relate_ingred_to_recipe(ingredient, recipe, quantity):
    ir = Ingredients_In_Recipe.objects.get_or_create(ingredient=ingredient,
                                                     recipe=recipe,
                                                     quantity=quantity)
    return ir

if __name__ == '__main__':
    print "Running population script v0.01"
    populate()
