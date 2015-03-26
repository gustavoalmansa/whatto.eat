from django.apps import AppConfig
import watson

class whatToEatConfig(AppConfig):
    name = "whatToEat"
    def ready(self):
        Recipe = self.get_model("Recipe")
        watson.register(Recipe, store=("slug","likes"))
        ingredients_in_recipe = self.get_model("Ingredients_In_Recipe")
        watson.register(ingredients_in_recipe)
	
