from django.contrib import admin
from whatToEat.models import UserProfile, Recipe, Ingredient, Inventory, ShoppingList, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Inventory)
admin.site.register(ShoppingList)
admin.site.register(Category)

