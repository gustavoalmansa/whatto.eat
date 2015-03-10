from django.conf.urls import patterns, url
from whatToEat import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))


