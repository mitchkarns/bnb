from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^$', views.view_all_or_search),
    url(r'^mypost/$', views.edit_or_create_post),
    url(r'^invite/$', views.invite_users),
    url(r'^login/$', login, kwargs={'template_name': 'temporary_housing/login.html'}),
    url(r'^swag/$', views.test),
    url(r'^profile/(?P<u>[0-9a-f]{32})/$', views.view_user),
    url(r'^logout/$', views.logout_view)

]
