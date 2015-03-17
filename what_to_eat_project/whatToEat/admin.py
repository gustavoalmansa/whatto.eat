from django.contrib import admin
from whatToEat.models import UserProfile, Recipe, Ingredients, Inventory, ShoppingList, Category

admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Inventory)
admin.site.register(ShoppingList)
admin.site.register(Category)
