from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.view_all_users, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', kwargs={
    'template_name': 'temporary_housing/login.html'}),
    url(r'^logout/$', views.logout_view)

]
