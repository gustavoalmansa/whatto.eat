from django.test import TestCase
from whatToEat.models import Recipe, Ingredients_In_Recipe, Ingredient, Category
from django.core.urlresolvers import reverse
import unittest

class RecipeMethodTests(TestCase):

    def setUp(self):
        Recipe.objects.create(name='test recipe', likes=0,
                              dislikes=0, author='author', category='dinner',
                              instructions='test')


    def Test_RatingisPositive(self):
        recipe = Recipe.objects.get(name="test recipe")
        recipe.save()
        print "Test 1 done"
        self.assertEqual((newrecipe.rating >= 0), True)


    def Test_CategoryIsNotAssumedCorrect(self):
        recipe = Recipe.objects.get(name="test recipe")
        recipe.save()
        print "Test 2 done"
        self.assertFalse(recipe.category, "lunch")

    def Test_SlugifyWorks(self):
        recipe = Recipe.objects.get(name="test recipe")
        recipe.save()
        print "Test 3 done"
        self.assertEqual(recipe.slug, "test-recipe")






class CategoryMethodTests(TestCase):

    def checkAddingRecipeWorks(self):
        newrecipe = recipe(name = 'testrecipe', likes = 0,
                           dislikes = 0, author=author_profile,
                           category="dinner", instructions = "test")
        newrecipe.save()
        recipes = Recipe.objects.filter(category="dinner")
        self.assertEquals((recipes.length > 0), True)




class unitTest(TestCase):

    def checkCorrectUnitTypesOnly(self):
        new = recipe(name = 'testrecipe', likes = 0,
                     dislikes = 0, author=author_profile,
                     category="dinner", instructions = "test")
        new.save()
        relateIngredientDictToRecipe({white_bread:[50, g]}, new)
        self.assertContains(new, "g")


class IndexViewTests(TestCase):

    def testIndexViewNoCats(self):
        response = self.client.get(reverse('index'))
        self.assertNotContains(response, "lunch")


class AllRecipeViewTests(TestCase):

    def noRecipes(self):
        response = self.client.get(reverse('all_recipes'))
        self.assertNotContains(response, "Mushroom")

    def addedRecipes(self):
        new = recipe(name = 'testrecipe', likes = 0,
                     dislikes = 0, author=author_profile,
                     category="dinner", instructions = "test")
        new.save()
        response = self.client.get(reverse('all_recipes'))
        self.assertContains(response, "testrecipe")


class RecipeViewTests(TestCase):

    def recipeHasInstructions(self):
        new = recipe(name = 'testrecipe', likes = 0,
                     dislikes = 0, author=author_profile,
                     category="dinner", instructions = "here are test instructions")
        new.save()
        response=self.client.get(reverse('recipe/testrecipe'))
        self.assertContains(response, "here are test instructions")