from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^$', views.view_all_or_search),
    url(r'^mypost/$', views.edit_or_create_post),
    url(r'^test/$', views.test),
    url(r'^invite/$', views.invite_users),
    url(r'^login/$', login, kwargs={'template_name': 'temporary_housing/login.html'}),
    url(r'^logout/$', views.logout_view)

]
