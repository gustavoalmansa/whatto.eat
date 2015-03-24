from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from whatToEat.forms import RecipeForm, IngredientForm, linkIngredientToRecipe
from whatToEat.models import Recipe, Category, Ingredients_In_Recipe, ShoppingList, Inventory, UserProfile, Ingredient
import json as simplejson


def index(request):
    context_dict = {}
    return render(request, 'whatToEat/index.html', context_dict)


def about(request):
    context_dict = ""
    return render(request, 'whatToEat/about.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        recipes = Recipe.objects.filter(category=category)
        context_dict['recipes'] = recipes
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'whatToEat/category.html', context_dict)


def recipe(request, recipe_name_slug):
    context_dict = {}
    try:
        recipe = Recipe.objects.get(slug=recipe_name_slug)
        context_dict['ingredient_list'] = []
        for ingred in Ingredients_In_Recipe.objects.filter(recipe=recipe):
            context_dict['ingredient_list'] += [ingred]

        context_dict['ingredient'] = ingred
        context_dict['recipe_name'] = recipe.name
        context_dict['recipe_rating'] = recipe.rating
        context_dict['recipe_instr'] = recipe.instructions
        context_dict['recipe_author'] = recipe.author
    except Recipe.DoesNotExist:
        pass

    return render(request, 'whatToEat/recipe.html', context_dict)


def add_recipe(request, category_name_slug):

    if request.method == 'POST':
        recipe_form = RecipeForm(data=request.POST)
        ingredient_form = IngredientForm(data=request.POST)
        link_form = linkIngredientToRecipe(data=request.POST)
        # Have we been provided with a valid form?
        if recipe_form.is_valid() and ingredient_form.is_valid() and link_form.is_valid():
            recipe = recipe_form.save(commit=False)
            print("Recipe name2: ", recipe.name)
            recipe.author = UserProfile.objects.get(user=request.user)
            recipe.category = Category.objects.get(slug=category_name_slug)
            recipe.save()
            print("Recipe name3: ", recipe.name)
            ingredient = ingredient_form.save()
            link = link_form.save(commit=False)
            link.recipe = recipe
            link.ingredient = ingredient
            link.save()
            print("Final recipe name: ", recipe.name)
            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (recipe_form.errors, ingredient_form.errors, link_form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        recipe_form = RecipeForm()
        ingredient_form = IngredientForm()
        link_form = linkIngredientToRecipe()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'whatToEat/add_recipe.html', {'recipe_form': recipe_form, 'ingredient_form': ingredient_form,
                                                         'link_form': link_form, 'category': category_name_slug})


@login_required
def profile(request):

    context_dict = {
        'all_ingredients': {}
    }
    try:
        all_ingredients = Ingredient.objects.order_by('name')
        context_dict['all_ingredients'] = all_ingredients
    except Ingredient.DoesNotExist:
        pass

    try:
        user = User.objects.get(username=request.user)
        user_profile = UserProfile.objects.get(user=user)
        ingredient_list = Inventory.objects.filter(user=user_profile)
        context_dict['user'] = user
        context_dict['user_profile'] = user_profile
        context_dict['ingredient_list'] = ingredient_list
    except UserProfile.DoesNotExist, Inventory.DoesNotExist:
        pass

    return render(request, 'whatToEat/profile.html', context_dict)


@login_required
def update_inventory(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            dict = {
                'status': 'failure',
                'quantity': '0',
                'ingredient': '0'
            }
            ingredient_id = request.POST.get('ingredient', 0)
            quantity = request.POST.get('quantity', 0)
            if ingredient_id != 0:
                ingredient = Ingredient.objects.get(id=ingredient_id)
                user = User.objects.get(username=request.user)
                user_profile = UserProfile.objects.get(user=user)
                row = Inventory.objects.get_or_create(user=user_profile, ingredient=ingredient)[0]
                row.quantity = quantity
                row.save()
                dict['status'] = 'success'
                dict['quantity'] = quantity
                dict['ingredient'] = ingredient_id
                dict['ingredientname'] = row.ingredient.name
            return HttpResponse(simplejson.dumps(dict), content_type="application/json")
        except Inventory.DoesNotExist:
            pass
        except User.DoesNotExist, UserProfile.DoesNotExist:
            pass
    else:
        return HttpResponse("Can't update via GET method")


def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/whatToEat/')
            else:
                return HttpResponse("Your whatToEat account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'accounts/login.html', {})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/whatToEat/')

def search_results(request):
    #TODO make function that actually searches recipes and returns them
    context_dict = {}
    
    context_dict['result_list'] = ['implement', 'search with results','to go here']


    return render(request, 'whatToEat/search.html', context_dict)
