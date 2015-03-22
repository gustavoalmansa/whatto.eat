from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from whatToEat.forms import RecipeForm
from whatToEat.models import Recipe, Category, Ingredients_In_Recipe, ShoppingList, Inventory, UserProfile, Ingredient
import json as simplejson


def index(request):
    category_list = Category.objects.all()[:6]
    recipe_list = Recipe.objects.order_by('-rating')[:10]
    context_dict = {'categories': category_list, 'recipes': recipe_list}
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
        context_dict['recipe_name'] = recipe.name
        context_dict['recipe_rating'] = recipe.rating
        context_dict['recipe_instr'] = recipe.instructions
        context_dict['recipe_author'] = recipe.author
    except Recipe.DoesNotExist:
        pass

    return render(request, 'whatToEat/recipe.html', context_dict)


def add_recipe(request, category_name_slug):

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            ##form.author_id = request.user
            ##form.save()

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = RecipeForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'whatToEat/add_recipe.html', {'form': form, 'category': category_name_slug})


# TODO: Remove comments of @login_required
# @login_required
def profile(request):
    # TODO: Add login functionality and and uncomment the request.user line
    context_dict = {}
    try:
        # TODO: Remove user comment
        # user = User.objects.get(username=request.user)
        user = User.objects.get(username="User 1")
        user_profile = UserProfile.objects.get(user=user)
        ingredient_list = Inventory.objects.filter(user=user_profile)
        context_dict['user_profile'] = user_profile
        context_dict['ingredient_list'] = ingredient_list
    except UserProfile.DoesNotExist, Inventory.DoesNotExist:
        pass

    return render(request, 'whatToEat/profile.html', context_dict)


# @login_required
def update_inventory(request):
    if request.method == "POST" and request.is_ajax():
        try:
            ingredient_id = request.POST.get("ingredient", 0)
            quantity = request.POST.get("quantity", 0)
            if quantity != 0 and ingredient_id != 0:
                ingredient = Ingredient.objects.get(id=ingredient_id)
                # TODO: Remove user comment and delete next line
                # user = User.objects.get(username=request.user)
                user = User.objects.get(username="User 1")
                user_profile = UserProfile.objects.get(user=user)
                row = Inventory.objects.get_or_create(user=user_profile, ingredient=ingredient)[0]
                row.quantity = quantity
                row.save()
            return HttpResponse("Test")
        except Inventory.DoesNotExist:
            pass
        except User.DoesNotExist, UserProfile.DoesNotExist:
            pass
    else:
        return HttpResponse("Can't update via GET method")