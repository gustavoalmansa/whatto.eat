from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView
from whatToEat import views

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/whatToEat/add_profile/'


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^whatToEat/', include('whatToEat.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_profile'), 
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', views.login_redirect , name='login_redirect'))
 
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
