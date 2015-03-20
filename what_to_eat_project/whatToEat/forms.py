from django import forms
from django.contrib.auth.models import User
from whatToEat.models import Ingredient, Recipe, Category, Inventory, ShoppingList, UserProfile

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the name of your recipe.")
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    instructions = forms.CharField(max_length=5000, help_text="Please enter all of the instructions:")

    class Meta:
        model = Recipe
        exclude = ('category', 'author', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile
#        fields = ('website', 'picture')