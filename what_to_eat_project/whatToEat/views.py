from django.http import HttpResponse
from django.shortcuts import render
from whatToEat.forms import RecipeForm
from whatToEat.models import Recipe, Category, Ingredients_In_Recipe, ShoppingList, Inventory


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
    except Recipe.DoesNotExist:
        pass

    return render(request, 'whatToEat/category.html', context_dict)


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
    return render(request, 'whatToEat/add_recipe.html', {'form': form, 'category':category_name_slug})

