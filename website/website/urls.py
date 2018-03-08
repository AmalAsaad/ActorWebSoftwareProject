from django.contrib import admin
from django.conf.urls import url,include
from actor import views
from django.conf import settings
from . import views
from homepage import views
from django.contrib.auth.views import login, logout
from actor.views import index
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #/
   #url(r'^$', views.contact, name='home'),
    url(r'^homepage/contact$', views.contact, name="contact"),

    #/actor
    url(r'^actor/', include('actor.urls')),

    url(r'^$', index  ),
   # url(r'^actor/logout/$',views., name='logout_redirect'),
   # url(r'^logout/$', views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

]

#urlpatterns = [



    #url(r'^admin/', admin.site.urls),
    #url(r'^actor/', include('actor.urls')),
    #url(r'^homepage/contact$', views.contact, name="contact"),
    #url(r'^login/$', login, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='profile'),
    #url(r'^', index, name="index"),

   #url(r'^$', index(request), name='index'),

    #/
  #  url(r'^$', views.homepage, name='home'),
#/actor

   # url(r'^actor/logout/$',views., name='logout_redirect'),
from django.contrib import admin
from django.conf.urls import url,include
from homepage import views
from website import views
from actor import views
from django.conf import settings





