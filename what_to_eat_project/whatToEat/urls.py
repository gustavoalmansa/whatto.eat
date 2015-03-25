from django.conf.urls import patterns, url
from whatToEat import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name='about'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_recipe/$', views.add_recipe, name='add_recipe'),
        url(r'^recipe/(?P<recipe_name_slug>[\w\-]+)/$', views.recipe, name='recipe'),
        url(r'^recipe/(?P<recipe_name_slug>[\w\-]+)/details/$', views.recipe_details, name='recipe_details'),
        url(r'^profile/', views.profile, name='profile'),
        url(r'^add_profile/', views.register_profile, name='add_profile'),
        url(r'^update-inventory/', views.update_inventory, name='update_inventory'),
        url(r'^update-recipe/', views.update_recipe, name='update_recipe'),
        url(r'^search/$', views.search_results, name='search'),
        url(r'^all_recipes/$', views.all_recipes, name='all_recipes'),
)


