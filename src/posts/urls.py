from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf.urls import url
from posts import views
from .views import(
	post_list,
	post_create,
	post_detail,
	post_update, 
	post_delete
	)

urlpatterns = [
    #path('posts/', "<appname>.views.<function_name>"),
    #re_path(r'', views.post_list, name ='list'),
    path('', views.post_list, name = 'list'),
    path('create/', views.post_create),
    re_path(r'^(?P<id>\d+)/$', views.post_detail, name ='detail'),
    re_path(r'^(?P<id>\d+)/edit/$', views.post_update, name ='update'),
    re_path(r'^(?P<id>\d+)/delete/$', views.post_delete, name = 'delete'),
]