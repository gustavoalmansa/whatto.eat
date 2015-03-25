from django import forms
from django.contrib.auth.models import User
from whatToEat.models import Ingredient, Recipe, Category, Inventory, ShoppingList, UserProfile, Ingredients_In_Recipe


class InitialRecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the name of your recipe.")
    print("Recipe name: ", name.__str__())

    class Meta:
        model = Recipe
        exclude = ('instructions', 'category', 'author', 'rating', 'slug')


class DetailRecipeForm(forms.ModelForm):
    instructions = forms.CharField(widget=forms.Textarea, max_length=5000)

    class Meta:
        model = Recipe
        exclude = ('name', 'category', 'author', 'rating', 'slug')


class IngredientForm(forms.ModelForm):
    ingredient_name = forms.CharField(max_length=100, help_text="Enter ingredient")

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
        exclude = ('user',)
