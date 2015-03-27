from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
import json
import watson
from string import digits

from whatToEat.forms import InitialRecipeForm, IngredientForm, linkIngredientToRecipe,\
    DetailRecipeForm, UserProfileForm, SearchForm

from whatToEat.models import Recipe, Category, Ingredients_In_Recipe, ShoppingList, Inventory, UserProfile, Ingredient, \
    Unit


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print "Search entered"

    else:
        form = SearchForm()
    return render(request, 'whatToEat/index.html', {'form': form})



def about(request):
    context_dict = ""
    return render(request, 'whatToEat/about.html', context_dict)

def all_recipes(request):
    context_dict = {}
    recipes = Recipe.objects.all().order_by("-rating")
    context_dict['recipes'] = recipes

    return render(request, 'whatToEat/all_recipes.html', context_dict)

def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        recipes = Recipe.objects.filter(category=category).order_by("-rating")
        context_dict['recipes'] = recipes
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'whatToEat/category.html', context_dict)


def recipe(request, recipe_name_slug):
    context_dict = {}
    response = render(request, 'whatToEat/recipe.html', context_dict)
    try:
        recipe = Recipe.objects.get(slug=recipe_name_slug)
        context_dict['ingredient_list'] = Ingredients_In_Recipe.objects.filter(recipe=recipe)
        context_dict['recipe'] = recipe
        if request.user == recipe.author.user:
            context_dict['same'] = True

        if request.method == 'POST':
            if "dislike" in request.POST:
                if 'disliked' and str(recipe.name) not in request.COOKIES:
                    recipe.dislikes += 1
                    recipe.save()
                    response.set_cookie('disliked', str(recipe.name))

            elif "like" in request.POST:
                if 'liked' and str(recipe.name) not in request.COOKIES:
                    recipe.likes += 1
                    recipe.save()
                    response.set_cookie('liked', str(recipe.name))

            response = render(request, 'whatToEat/recipe.html', context_dict)

    except Recipe.DoesNotExist:
        return redirect('/404/')

    return response


def recipe_details(request, recipe_name_slug):

    recipe = Recipe.objects.get(slug=recipe_name_slug)

    context_dict = {
        'all_ingredients': {}
    }
    try:
        all_ingredients = Ingredient.objects.order_by('ingredient_name')
        context_dict['all_ingredients'] = all_ingredients
    except Ingredient.DoesNotExist:
        pass

    if request.method == 'POST':
        recipe_form = DetailRecipeForm(data=request.POST)

        if recipe_form.is_valid():
            instructions = recipe_form.save(commit=False)
            instructions = instructions.instructions
            recipe.instructions = instructions
            recipe.save()

        return HttpResponseRedirect('/whatToEat/recipe/'+recipe.slug+"/")
    else:
        # If the request was not a POST, display the form to enter details.
        try:
            used_ingredients = Ingredients_In_Recipe.objects.filter(recipe=recipe)
            context_dict['used_ingredients'] = used_ingredients
        except Ingredients_In_Recipe.DoesNotExist:
            pass

        recipe_form = DetailRecipeForm(None, initial={"instructions": recipe.instructions})

    context_dict['recipe_form'] = recipe_form
    context_dict['recipe'] = recipe

    if request.user == recipe.author.user:
        return render(request, 'whatToEat/add_recipe_details.html', context_dict)
    else:
        return HttpResponseRedirect('/whatToEat/recipe/'+recipe.slug+"/")


def add_recipe(request, category_name_slug):

    if request.method == 'POST':
        recipe_form = InitialRecipeForm(data=request.POST)
        ingredient_form = IngredientForm(data=request.POST)
        link_form = linkIngredientToRecipe(data=request.POST)
        # Have we been provided with a valid form?
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = UserProfile.objects.get(user=request.user)
            recipe.category = Category.objects.get(slug=category_name_slug)
            recipe.save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return HttpResponseRedirect("/whatToEat/recipe/" + recipe.slug + "/details/")
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (recipe_form.errors, ingredient_form.errors, link_form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        recipe_form = InitialRecipeForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'whatToEat/add_recipe.html', {'recipe_form': recipe_form, 'category': category_name_slug})


def register_profile(request):

    # A HTTP POST?
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = form.save(commit=False)
            profile.user = request.user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()
            # Now call the index() view.
            # The user will be shown the homepage.
            return HttpResponseRedirect('/whatToEat/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        form = 6
    return render(request, 'whatToEat/profile_registration.html', {'form': form})


@login_required
def profile(request):

    context_dict = {
        'all_ingredients': {},
        'all_units': {}
    }
    try:
        all_ingredients = Ingredient.objects.order_by('ingredient_name')
        context_dict['all_ingredients'] = all_ingredients
    except Ingredient.DoesNotExist:
        pass

    try:
        all_units = Unit.objects.all()
        context_dict['all_units'] = all_units
    except Unit.DoesNotExist:
        pass

    try:
        user = User.objects.get(username=request.user)
        user_profile = UserProfile.objects.get(user=user)
        ingredient_list = Inventory.objects.filter(user=user_profile)
        recipe_list = Recipe.objects.filter(author=user_profile)
        context_dict['recipe_list'] = recipe_list
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
                'ingredient': '0',
                'unit': '0'
            }
            ingredient_id = request.POST.get('ingredient', 0)
            quantity = request.POST.get('quantity', 0)
            unit_id = request.POST.get('unit', 0)
            if ingredient_id != 0 and unit_id != 0:
                unit = Unit.objects.get(id=unit_id)
                ingredient = Ingredient.objects.get(id=ingredient_id)
                user = User.objects.get(username=request.user)
                user_profile = UserProfile.objects.get(user=user)
                row = Inventory.objects.get_or_create(user=user_profile, ingredient=ingredient)[0]
                row.quantity = quantity
                row.unit = unit
                row.save()
                dict['status'] = 'success'
                dict['quantity'] = quantity
                dict['ingredient'] = ingredient_id
                dict['ingredientname'] = row.ingredient.ingredient_name
                dict['unit'] = unit_id
            return HttpResponse(json.dumps(dict), content_type="application/json")
        except Inventory.DoesNotExist:
            pass
        except User.DoesNotExist, UserProfile.DoesNotExist:
            pass
    else:
        return HttpResponse("Can't update via GET method")


@login_required
def delete_inventory(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            dict = {
                'status': 'failure',
                }
            ingredient_id = request.POST.get('ingredient', 0)
            if ingredient_id != 0:
                ingredient = Ingredient.objects.get(id=ingredient_id)
                user = User.objects.get(username=request.user)
                user_profile = UserProfile.objects.get(user=user)
                row = Inventory.objects.get_or_create(user=user_profile, ingredient=ingredient)[0]
                row.delete()
                dict['status'] = 'success'
                dict['ingredient'] = ingredient_id
            return HttpResponse(json.dumps(dict), content_type="application/json")
        except Inventory.DoesNotExist:
            pass
        except User.DoesNotExist, UserProfile.DoesNotExist:
            pass
    else:
        return HttpResponse("Can't update via GET method")


@login_required
def update_recipe(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            dict = {
                'status': 'failure',
                'quantity': '0',
                'ingredient': '0',
                'recipe': '0',
                }
            ingredient_id = request.POST.get('ingredient', 0)
            recipe_id = request.POST.get('recipe', 0)
            quantity = request.POST.get('quantity', 0)
            if ingredient_id != 0:
                ingredient = Ingredient.objects.get(id=ingredient_id)
                recipe = Recipe.objects.get(id=recipe_id)
                row = Ingredients_In_Recipe.objects.get_or_create(recipe=recipe, ingredient=ingredient)[0]
                row.quantity = quantity
                row.save()
                dict['status'] = 'success'
                dict['quantity'] = quantity
                dict['ingredient'] = ingredient_id
                dict['ingredientname'] = row.ingredient.ingredient_name
            return HttpResponse(json.dumps(dict), content_type="application/json")
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
    context_dict = {}

    if request.method == 'POST':
        recipes = []
        search_terms = request.POST["search"]
        searchResults = watson.search(search_terms)
        # Gets search results which aren't ingredients
        c = 0
        while c < len(searchResults):
            if str(searchResults[c])[0] not in digits:
                recipes += [Recipe.objects.get(name=searchResults[c])]
            c += 1
        if len(recipes) > 0:
            context_dict['result_list'] = recipes


    return render(request, 'whatToEat/search.html', context_dict)


def login_redirect(request):
    url = '/whatToEat/'
    return redirect(url)

