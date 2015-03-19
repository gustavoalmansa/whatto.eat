from django.http import HttpResponse
from django.shortcuts import render
from whatToEat.models import Recipe, Category, Ingredients_In_Recipe, ShoppingList, Inventory


def index(request):
    category_list = Category.objects.all()[:6]
    context_dict = {'categories' : category_list}
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

    return render(request, 'rango/category.html', context_dict)