from django.apps import AppConfig
import watson

class whatToEatConfig(AppConfig):
    name = "whatToEat"
    def ready(self):
        Recipe = self.get_model("Recipe")
        watson.register(Recipe)
