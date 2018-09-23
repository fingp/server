from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^board', views.board),
    url(r'^login', views.login),
    url(r'^getassignment', views.getassignment),
]