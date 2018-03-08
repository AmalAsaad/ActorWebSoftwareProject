from django.conf.urls import url
from actor import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # /actor/1
    url(r'^(?P<actor_id>[0-9]+)$', views.details, name='details'),
    #/actor/1/review
    url(r'^(?P<actor_id>[0-9]+)/review$', views.review, name='review'),
    # /actor/1/message
    url(r'^(?P<actor_id>[0-9]+)/message$', views.message, name='message'),
    # /actor/create
    url(r'^create$', views.create, name="create"),

    # /actor/1/edit
    url(r'^(?P<actor_id>[0-9]+)/edit$', views.edit, name="edit"),

    # /actor/1/delete
    url(r'^(?P<actor_id>[0-9]+)/delete$', views.delete, name="delete"),
    # /actor/search
    url(r'^search$', views.search, name="search"),
    # /actor/register
    url(r'^register$', views.UserFormView, name="register"),

    # /actor/login
    url(r'^login/$', login, {"template_name": "actor/login.html"}),

    # /actor/logout
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    #url(r'^logout/$', logout, {"template_name": "actor/logout.html"}),

    # /actor/profile
    url(r'^profile/$', views.view_profile, name='view_profile'),
    # /actor/profile/edit
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),

    # /actor/change_password
    url(r'^profile/change_password$', views.change_password, name='change_password'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)