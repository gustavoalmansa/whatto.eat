from django.conf.urls import patterns, url
from whatToEat import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name='about'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_recipe/$', views.add_recipe, name='add_recipe'),
        url(r'^recipe/(?P<recipe_name_slug>[\w\-]+)/$', views.recipe, name='recipe'),
        url(r'^profile/', views.profile, name='profile'),
)


