from django.test import TestCase
from whatToEat.models import Recipe, Ingredients_In_Recipe, Ingredient, Category
from django.core.urlresolvers import reverse

class RecipeMethodTests(TestCase):

    def ensureRatingisPositive(self):
        # TODO


    def ensureAuthorisUser(self):
        # TODO

    def checkSlugifyWorks(self):
        # TODO


class CategoryMethodTests(TestCase):

    def checkSlugifyWorks(self):
        # TODO


class unitTest(TestCase):

    def checkCorrectUnitTypesOnly(self):
        # TODO


class IndexViewTests(TestCase):

    def testIndexViewNoCats(self):
        # TODO


class AllRecipeViewTests(TestCase):

    def noRecipes(self):
        # TODO

    def addedRecipes(self):
        # TODO


class RecipeViewTests(TestCase):

    def recipeHasInstructions(self):
        # TODO