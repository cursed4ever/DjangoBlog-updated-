from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^posts/', views.posts_home),
    url(r'^create$', "posts.views.posts_create"),
    url(r'^$', "posts.views.posts_list"),
    url(r'^delete$', "posts.views.posts_delete"),
    url(r'^detail/(?P<id>\d+)/$', "posts.views.posts_details", name = 'detail'),
    url(r'^update$', "posts.views.posts_update"),

]