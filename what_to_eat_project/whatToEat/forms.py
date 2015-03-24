from django import forms
from django.contrib.auth.models import User
from whatToEat.models import Ingredient, Recipe, Category, Inventory, ShoppingList, UserProfile, Ingredients_In_Recipe

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the name of your recipe.")
    instructions = forms.CharField(max_length=5000, help_text="Please enter all of the instructions:")
    print("Recipe name: ", name.__str__())

    class Meta:
        model = Recipe
        exclude = ('category', 'author', 'rating', 'slug')


class IngredientForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter ingredient")

    class Meta:
        model = Ingredient

class linkIngredientToRecipe(forms.ModelForm):

    quantity = forms.CharField(max_length=100, help_text="Quantity")
    class Meta:
        model = Ingredients_In_Recipe
        exclude = ("recipe", "ingredient")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user',)
