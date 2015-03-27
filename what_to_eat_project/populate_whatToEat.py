import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'what_to_eat_project.settings')

import django
django.setup()

from whatToEat.models import Ingredient, Recipe, Category, UserProfile, Inventory, Ingredients_In_Recipe, Unit
from django.contrib.auth.models import User


def populate():

    for i in xrange(15):
        u = User(username="User "+str(i))
        u.set_password("q")
        u.save()
        add_profile(u)

    author_profile = add_profile(User.objects.get(username="User 1"))
    print("Users added")

    ml = add_unit("ml")
    g = add_unit("g")
    arbitrary = add_unit(" ")

    print("Units added")
    print("Adding ingredients")
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
    tinned_tomatoe = add_ingred("Tinned Tomatoes")
    ground_beef = add_ingred("Ground Beef")
    ground_turkey = add_ingred("Ground Turkey")
    alfredo_sauce =  add_ingred("Alfredo Sauce")
    almonds =  add_ingred("Almonds")
    allspice =  add_ingred("Allspice")
    anise =  add_ingred("Anise")
    amaretto = add_ingred("Amaretto")
    bacon = add_ingred("Bacon")
    bagel =  add_ingred("Bagel")
    baking_soda =  add_ingred("Baking Soda")
    baking_power =  add_ingred("Baking Powder")
    balsamic =  add_ingred("Balsamic Vinegar")
    bamboo =  add_ingred("bamboo shoots")
    banana =  add_ingred("bananas")
    bbq =  add_ingred("Barbecue Sauce")
    barley =  add_ingred("Barley")
    basil =  add_ingred("Basil")
    dry_basil =  add_ingred("Dried Basil")
    basmati_rice =  add_ingred("Basmati Rice")
    bass =  add_ingred("Bass")
    bay_leaf =  add_ingred("Bay Leaves")
    black_bean =  add_ingred("Black Beans")
    bean =  add_ingred("Beans")
    bean_sprout =  add_ingred("Bean Sprouts")
    beetroot =  add_ingred("Beets")
    beef =  add_ingred("Beef")
    beer =  add_ingred("Beer")
    raspberries =  add_ingred("Raspberries")
    blueberries =  add_ingred("Blueberries")
    blackberries =  add_ingred("Blackberries")
    biscuit =  add_ingred("Biscuits")
    black_olives =  add_ingred("Black Olives")
    blue_cheese =  add_ingred("Blue Cheese")
    brown_rice =  add_ingred("Brown Rice")
    broccoli =  add_ingred("Broccoli")
    beef_broth =  add_ingred("Beef Broth")
    chicken_broth =  add_ingred("Chicken Broth")
    apple =  add_ingred("Apples")
    applesauce =  add_ingred("Applesauce")
    apricots =  add_ingred("Apricots")
    apricot_jam =  add_ingred("Apricot Jam")
    artichokes =  add_ingred("Artichokes")
    asafetida =  add_ingred("Asafetida")
    asparagus =  add_ingred("Asparagus")
    avocado =  add_ingred("Avocados")
    breadcrumbs =  add_ingred("Breadcrumbs")
    buttermilk =  add_ingred("Buttermilk")
    cabbage =  add_ingred("Cabbage")
    cacaopowder =  add_ingred("Cacao Powder")
    cactus =  add_ingred("Cactus")
    cannellini_beans =  add_ingred("Cannellini Beans")
    cantaloupes =  add_ingred("Cantaloupes")
    capers =  add_ingred("capers")
    capsicum =  add_ingred("Capsicum")
    cardamom =  add_ingred("Cardamom")
    carrot =  add_ingred("Carrots")
    cashew =  add_ingred("Cashew")
    catfish =  add_ingred("Catfish")
    cayenne =  add_ingred("Cayenne Pepper")
    cauliflower =  add_ingred("Cauliflower")
    caviar =  add_ingred("Caviar")
    celery =  add_ingred("Celery")
    celeriac =  add_ingred("Celeriac")
    cheese =  add_ingred("Cheese")
    cherry =  add_ingred("Cherries")
    chicken =  add_ingred("Chicken")
    chickpeas = add_ingred("Chickpeas")
    chicken_liver =  add_ingred("Chicken Liver")
    chives = add_ingred("Chives")
    chili_power =  add_ingred("Chili Powder")
    chilis =  add_ingred("Chili Peppers")
    milk_chocolate =  add_ingred("Milk Chocolate")
    white_choolcate =  add_ingred("White Chocolate")
    dark_chocolate =  add_ingred("Dark Chocolate")
    crayfish =  add_ingred("Crayfish")
    cottagecheese =  add_ingred("Cottage Cheese")
    coriander =  add_ingred("Coriander")
    corn_flour =  add_ingred("Corn Flour")
    couscous =  add_ingred("Couscous")
    crab =  add_ingred("Crab")
    creamcheese =  add_ingred("Cream Cheese")
    creamoftartar =  add_ingred("Cream Of Tartar")
    cream =  add_ingred("Cream")
    coffee =  add_ingred("Coffee")
    cumin =  add_ingred("Cumin")
    curry =  add_ingred("Curry")
    cucumbers =  add_ingred("Cucumbers")
    custard =  add_ingred("Custard")
    cookingwine =  add_ingred("Cooking Wine")
    coconut =  add_ingred("Coconut")
    cod =  add_ingred("Cod")
    cloves =  add_ingred("Cloves")
    cinnamon =  add_ingred("Cinnamon")
    dates =  add_ingred("Dates")
    dill =  add_ingred("Dill")
    duck =  add_ingred("Duck")
    dumpling =  add_ingred("Dumplings")
    eggwhite =  add_ingred("Egg Whites")
    eggyolk =  add_ingred("Egg Yolk")
    falafel =  add_ingred("Falafel")
    foiegras =  add_ingred("Foie Gras")
    fennel =  add_ingred("Fennel")
    fennelseeds =  add_ingred("Fennel Seeds")
    fenugreek =  add_ingred("Fenugreek")
    fetacheese =  add_ingred("Feta Cheese")
    figs =  add_ingred("Figs")
    fishsauce =  add_ingred("Fish Sauce")
    ground_pork =  add_ingred("Ground Pork")
    fivespice =  add_ingred("Five Spice Powder")
    flaxseed =  add_ingred("Flax Seed")
    flounder =  add_ingred("Flounder")
    focaccia =  add_ingred("Focaccia")
    flour =  add_ingred("Flour")
    garlic =  add_ingred("Garlic")
    garlic_powder =  add_ingred("Garlic Powder")
    ghee =  add_ingred("Ghee")
    ginger =  add_ingred("Ginger")
    golden_syrup =  add_ingred("Golden Syrup")
    grandmarnier =  add_ingred("Grand Marnier")
    grapefruit =  add_ingred("Grapefruit")
    gravy = add_ingred("Gravy")
    granola =  add_ingred("Granola")
    greenbeans =  add_ingred("Greenbeans")
    greenonions =  add_ingred("Green Onions")
    guava =  add_ingred("Guava")
    habanero =  add_ingred("Habanero")
    haddock =  add_ingred("Haddock")
    hazelnuts =  add_ingred("Hazelnuts")
    hoisinsauce =  add_ingred("Hoisin Sauce")
    horseradish =  add_ingred("Horseradish")
    hotsauce =  add_ingred("Hot Sauce")
    icingsugar =  add_ingred("Icing Sugar")
    icecream =  add_ingred("Ice Cream")
    irishcream =  add_ingred("Irish Cream")
    strawjam =  add_ingred("Strawberry Jam")
    rasjam =  add_ingred("Raspberry Jam")
    jelly =  add_ingred("Jelly")
    kale =  add_ingred("Kale")
    kidneybean =  add_ingred("Kidney Beans")
    lamb =  add_ingred("Lamb")
    kiwi =  add_ingred("Kiwi")
    lime =  add_ingred("Limes")
    liver =  add_ingred("Liver")
    ladyfingers =  add_ingred("Ladyfingers")
    marscapone =  add_ingred("Marscapone Cheese")
    espresso =  add_ingred("Espresso")
    lemonpeel =  add_ingred("Lemon Peel")
    lentils =  add_ingred("Lentils")
    lobster =  add_ingred("Lobster")
    lettuce =  add_ingred("Lettuce")
    leeks =  add_ingred("Leeks")
    macaroni =  add_ingred("Macaroni")
    mahimahi =  add_ingred("Mahi Mahi")
    maltvingar =  add_ingred("Malt Vinegar")
    mandarinorange =  add_ingred("Mandarin Oranges")
    mango =  add_ingred("Mangoes")
    print("50% of ingredients added..")
    margarine =  add_ingred("Margarine")
    maplesyrup =  add_ingred("Maple Syrup")
    marmalade =  add_ingred("Marmalade")
    marshmallow =  add_ingred("Marshmallows")
    marzipan =  add_ingred("Marzipan")
    masala =  add_ingred("Masala")
    mayonnaise =  add_ingred("Mayonnaise")
    melons = add_ingred("Melons")
    meringue =  add_ingred("Meringue")
    mint =  add_ingred("Mint")
    molasses =  add_ingred("Molasses")
    monkfish =  add_ingred("Monkfish")
    mozzarella = add_ingred("Mozzarella Cheese")
    muscovado =  add_ingred("Muscovado Sugar")
    mustard =  add_ingred("Mustard")
    mustardseed =  add_ingred("Mustard Seed")
    nectarines =  add_ingred("Nectarines")
    oatmeal =  add_ingred("Oatmeal")
    octopus =  add_ingred("Octopus")
    okra =  add_ingred("Okra")
    greenolives =  add_ingred("Green Olives")
    onion =  add_ingred("Onions")
    orange =  add_ingred("Orange")
    orangejuice =  add_ingred("Orange Juice")
    oregano =  add_ingred("Oregano")
    oystersauce =  add_ingred("Oyster Sauce")
    paprika =  add_ingred("Paprika")
    parmesan =  add_ingred("Parmesan Cheese")
    parsley =  add_ingred("Parsley")
    parsnips =  add_ingred("Parsnips")
    passion =  add_ingred("Passion Fruit")
    peas =  add_ingred("Peas")
    peaches =  add_ingred("Peaches")
    peanuts =  add_ingred("Peanuts")
    peanutbutter =  add_ingred("Peanut Butter")
    pears =  add_ingred("Pears")
    persimmons =  add_ingred("Persimmons")
    pesto =  add_ingred("Pesto")
    pickles =  add_ingred("Gherkins")
    pickle =  add_ingred("Pickle")
    pecans =  add_ingred("Pecans")
    pike =  add_ingred("Pike")
    pinenuts =  add_ingred("Pine Nuts")
    pineapples =  add_ingred("Pineapple")
    pistachios =  add_ingred("Pistachio")
    plantains =  add_ingred("Plantains")
    plums =  add_ingred("Plums")
    tomatoes =  add_ingred("Tomatoes")
    pomegranates =  add_ingred("Pomegranates")
    potatoe =  add_ingred("Potatoes")
    pork =  add_ingred("Pork")
    portabellas =  add_ingred("Portobello Mushrooms")
    powderedsugar =  add_ingred("Powdered Sugar")
    prosciutto =  add_ingred("Prosciutto")
    puffpastry =  add_ingred("Puff Pastry")
    pumpkin =  add_ingred("Pumpkin")
    pumpkinseeds =  add_ingred("Pumpkin Seeds")
    quaileggs =  add_ingred("Quail Eggs")
    quark =  add_ingred("Quark")
    tortilla =  add_ingred("Tortillas")
    picodegallo =  add_ingred("Pico De Gallo")
    quinoa =  add_ingred("Quinoa")
    radishes =  add_ingred("Radishes")
    raisin =  add_ingred("Raisins")
    redcabbage =  add_ingred("Red Cabbage")
    redleicester =  add_ingred("Red Leicester Cheese")
    rhubarb =  add_ingred("Rhubarb")
    ricevinegar =  add_ingred("Rice Vinegar")
    ricottacheese =  add_ingred("Ricotta Cheese")
    romainelettuce =  add_ingred("Romaine Lettuce")
    rosewater =  add_ingred("Rose Water")
    rosemary =  add_ingred("Rosemary")
    roux =  add_ingred("Roux")
    rum =  add_ingred("Rum")
    sage =  add_ingred("Sage")
    salmon =  add_ingred("Salmon")
    salsa =  add_ingred("Salsa")
    wholewheatbread =  add_ingred("Whole Wheat Bread")
    sesameseed =  add_ingred("Sesame Seeds")
    shrimp =  add_ingred("Shrimp")
    smokedsalmon =  add_ingred("Smoked Salmon")
    snappeas =  add_ingred("Snap Peas")
    satay =  add_ingred("Satay Sauce")
    shallots =  add_ingred("Shallots")
    sherry =  add_ingred("Sherry")
    sourcream =  add_ingred("Sour Cream")
    soymilk =  add_ingred("Soymilk")
    soybeans =  add_ingred("Soybeans")
    tofu =  add_ingred("Tofu")
    sugar =  add_ingred("Sugar")
    spinach =  add_ingred("Spinach")
    squid =  add_ingred("Squid")
    staranise =  add_ingred("Star Anise")
    steak =  add_ingred("Steak")
    stevia =  add_ingred("Stevia")
    stilton =  add_ingred("Stilton")
    strawberries =  add_ingred("Strawberries")
    sweetpotatoe =  add_ingred("Sweet Potatoes")
    condensedmilk =  add_ingred("Condensed Milk")
    swisscheese =  add_ingred("Swiss Cheese")
    swordfish =  add_ingred("Swordfish")
    sweetchilisauce =  add_ingred("Sweet Chili Sauce")
    tabascosauce =  add_ingred("Tabasco Sauce")
    tamarind =  add_ingred("Tamarind")
    tandooripaste =  add_ingred("Tandoori Paste")
    tarragon =  add_ingred("Tarragon")
    tempeh =  add_ingred("Tempeh")
    thyme =  add_ingred("Thyme")
    tofu = add_ingred("Tofu")
    trout =  add_ingred("Trout")
    tomatopaste =  add_ingred("Tomato Paste")
    tomatosauce =  add_ingred("Tomato Sauce")
    tonicwater =  add_ingred("Tonic Water")
    tuna = add_ingred("Tuna")
    turkey =  add_ingred("Turkey")
    turmericpowder =  add_ingred("Turmeric Powder")
    trumeric =  add_ingred("Turmeric")
    turnips =  add_ingred("Turnips")
    vanilla =  add_ingred("Vanilla Beans")
    vanillaextract =  add_ingred("Vanilla extract")
    venison =  add_ingred("Venison")
    vinegar =  add_ingred("Vinegar")
    vermouth =  add_ingred("Vermouth")
    walnuts =  add_ingred("Walnuts")
    wasabi =  add_ingred("Wasabi")
    waterchestnut =  add_ingred("Water Chestnuts")
    water =  add_ingred("Water")
    watercress =  add_ingred("Watercress")
    watermelon =  add_ingred("Watermelon")
    wheatgerm =  add_ingred("Wheat Germ")
    whitebeans =  add_ingred("White Beans")
    wildrice =  add_ingred("Wild Rice")
    wine =  add_ingred("Red Wine")
    whitewine =  add_ingred("White Wine")
    worchestershiresauce =  add_ingred("Worcestershire Sauce")
    yeast =  add_ingred("Fresh Yeast")
    dryyeast =  add_ingred("Dry Yeast")
    yogurt =  add_ingred("Yogurt")
    zucchini =  add_ingred("zucchini")
    lemonzest =  add_ingred("Lemon Zest")
    orangezest =  add_ingred("Orange Zest")



    print("Ingredients added")

    breakfast =add_cat("Breakfast")
    lunch = add_cat("Lunch")
    snack  = add_cat("Snacks")
    dinner  = add_cat("Dinner")
    dessert = add_cat("Dessert")
    print("Categories added")

    mushroomOmlette = add_recipe(name="Mushroom omelette", likes=4, dislikes=1, author=author_profile, category=lunch,
                                 instructions="<br>1) Crack the eggs into a mixing bowl "
                                              "<br>2) Add a pinch of salt and pepper"
                                              "<br>3) Beat well with a fork Quarter or roughly chop the mushrooms and add to a small frying"
                            " pan on a high heat with a small knob of butter, a drizzle of olive oil and a pinch of "
                            "salt and pepper"
                            "<br>4) Fry and toss around until golden, then turn the heat down to medium "
                            "<br>5) Add your eggs and move the pan around to spread them out evenly "
                            "<br>6) When the omelette begins to cook and firm up, but still has a little raw egg on top,"
                            " sprinkle over the Cheddar, if using "
                            "<br>7) Ease around the edge of the omelette with a spatula, then fold it in half "
                            "<br>8) When it starts to turn golden brown underneath, remove the pan from the heat and "
                            "slide the omelette on to a plate")
    print("Recipe added")

    relateIngredientDictToRecipe({egg_ingredient:[2, arbitrary],
                                  salt:[.5, g],
                                  pepper:[.5, g],
                                  butter:[5, g],
                                  olive_oil:[10, ml],
                                  cheddar_cheese:[10, g],
                                  mushroom:[3, arbitrary]},
                                 mushroomOmlette)

    add_ingredient_to_inventory(author_profile, 2, arbitrary, chicken_breast)
    add_ingredient_to_inventory(author_profile, 3, arbitrary,  egg_ingredient)
    print("Ingredients added to inventory")

    cheeseOnionRarebit = add_recipe(name="Quick Cheese and Onion Rarebit",
                                    likes=3, dislikes=1, author=author_profile,
                                    category=snack,
                                    instructions = "<br>1)Toast the bread in a toaster. Meanwhile, mix the cheese sauce,"
                                                   " onions and a grind of pepper together in a small bowl."
                                                   "<br>2)Transfer the toast to a non-stick grill rack and drape the ham"
                                                   " over each slice. Next, spoon the cheese sauce onto the ham and spread it around with the back of "
                                                   "the spoon. Scatter the grated cheese over the sauce, then pop the "
                                                   "rarebit under a hot grill until the cheese turns bubbly and golden. "
                                                   "<br>3)Cut each slice in half and serve while still hot.")


    relateIngredientDictToRecipe({white_bread:[50, g],
                                  four_cheese_sauce:[350, g],
                                  spring_onion:[3, arbitrary],
                                  sliced_ham:[100, g],
                                  cheddar_cheese:[50, g]},
                                cheeseOnionRarebit)

    honeyGlazedChicken = add_recipe(name = "Honey Glazed Chicken",
                                    likes=5, dislikes=1,
                                    author = author_profile,
                                    category=dinner,
                                    instructions = "1)Put 2 chicken breasts, skin side up in a small baking dish and season."
                                                   "<br>2)Squeeze the lemon into a bowl and stir in the honey and soy sauce. Spoon the mixture over the chicken, "
                                                   "then tuck the squeezed-out half of lemon between the pieces (this will moisten and add flavour to the chicken)."
                                                   "<br>3)Roast the chicken breasts in a baking dish, uncovered, for 30-35 minutes in a preheated oven (190C/gas 5/fan oven 170C). "
                                                   "4)Cook until done and richly glazed, basting with the juices at least twice. To check if they are done, prod the chicken with your"
                                                   " finger - if it's still a bit soft, give it a bit longer."
                                                   "<br>5)Serve with salad and potatoes roasted with herbs and garlic.")


    relateIngredientDictToRecipe({chicken_breast:[2, arbitrary],
                                  lemon:[.5, arbitrary],
                                  honey:[15, g],
                                  soy_sauce:[15, g]},
                                 honeyGlazedChicken)

    stickyChickenDrumstick = add_recipe("Sticky Chicken Drumstick",
                                        likes = 4, dislikes=1, author = author_profile,
                                        category=dinner,
                                        instructions="<br>1)Make 3 slashes on each of the drumsticks. Mix together the soy, honey, oil,"
                                                     " tomato puree and mustard. Pour this mixture over the chicken and coat thoroughly. "
                                                     "Leave to marinate for 30 mins at room temperature or overnight in the fridge. Heat oven to 200C/fan 180C/gas 6."
                                                     "<br>2)Tip the chicken into a shallow roasting tray and cook for 35 mins, turning occasionally, "
                                                     "until the chicken is tender and glistening with the marinade.")

    relateIngredientDictToRecipe({chicken_drumstick:[8, arbitrary],
                                  soy_sauce:[30, ml],
                                  honey:[15, ml],
                                  olive_oil:[15, ml],
                                  tomato_puree: [15, ml],
                                  dijon:[1, ml]},
                                 stickyChickenDrumstick)

    chocolatesouflee = add_recipe("Basic Chocolate Souflee", likes = 5,
                                  dislikes=1, author = author_profile,
                                  category = dessert,
                                  instructions = "<br>1)Brush four 200ml souffle dishes and brush them with softened butter. "
                                                 "Chill them for 5 minutes and then coat each lightly with some grated dark chocolate. "
                                                 "<br>2) For the custard cream, mix flour, sugar, and cornflour. Put egg yolk and whole egg"
                                                 " into a bowl, stir, then beat in half of the flour mixture to give a smooth paste. Tip in"
                                                 " the rest of the flour mixture and mix well. "
                                                 "<br>3) Pour the milk and cream into a pan and bring "
                                                 "just to a boil. Remove from the heat, and add chocolate to mix until smooth. "
                                                 "<br>4) Slowly mix chocolate into the custard cream over light heat until it is a thick paste. "
                                                 "Then leave it to cool as you make the ganache. "
                                                 "<br>5)Slowly warm cream in a pan. Just before it boils, take off the heat and add chocolate and "
                                                 "beat until it has a velvetty texture. Allow this to cool as well. "
                                                 "<br>6)Heat up the oven to 190 degrees Celsius. Whisk your egg whites until they have soft peaks. "
                                                 "<br>7) Mix the cream and ganache, and then carefully fold in the egg whites. "
                                                 "<br>8)Spoon the egg white and cream mixture into each dish, filling it up 2/3s of the way. "
                                                 "Bang the dishes down a bit to ensure that the dishes are filled completely, and then even out "
                                                 "with a palette knife. "
                                                 "<br>9) Put the souffles in the oven for about 15 minutes. "
                                                 "<br>10) When risen, take out of the oven and serve as soon as possible.")

    relateIngredientDictToRecipe({butter : [25, g],
                                  flour : [30, g],
                                  sugar : [5, g],
                                  eggyolk : [1, arbitrary],
                                  egg_ingredient : [1, arbitrary],
                                  milk : [100, ml],
                                  cream : [100, ml],
                                  dark_chocolate : [50, g],
                                  eggwhite: [6, arbitrary],
                                  cacaopowder:[60, g]},
                                 chocolatesouflee)
    print ("Recipes added, and ingredients related")


def add_profile(user):
    up = UserProfile.objects.get_or_create(user=user)[0]
    return up


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


def add_ingred(name):
    i = Ingredient.objects.get_or_create(ingredient_name=name)[0]
    return i


def relateIngredientDictToRecipe(ingredientDict, recipe):
    for ingredient in ingredientDict:
        relate_ingred_to_recipe(ingredient, recipe, ingredientDict[ingredient][0], ingredientDict[ingredient][1])


def add_recipe(name, likes, dislikes, author, category, instructions):
    r = Recipe.objects.get_or_create(name=name, likes=likes, dislikes=dislikes,
                                     rating=likes-dislikes,
                                     author=author, category=category,
                                     instructions=instructions)[0]
    return r


def add_ingredient_to_inventory(user_profile, quantity, unit, ingredient):
    i = Inventory.objects.get_or_create(
        user=user_profile,
        quantity=quantity,
        unit = unit,
        ingredient=ingredient)[0]
    return i


def relate_ingred_to_recipe(ingredient, recipe, quantity, unit):
    ir = Ingredients_In_Recipe.objects.get_or_create(ingredient=ingredient,
                                                     recipe=recipe,
                                                     quantity=quantity, unit = unit)
    return ir


def add_unit(name):
    unit = Unit.objects.get_or_create(unit_name=name)[0]
    return unit

if __name__ == '__main__':
    print "Running population script v0.01"
    populate()
