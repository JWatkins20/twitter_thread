from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth import views as authviews
from .views import *

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^login/$', authviews.LoginView.as_view(), name='login'),
	url(r'^logout/$', authviews.LogoutView.as_view(), name='logout'),
	url(r'^oauth/', include('social_django.urls', namespace='social')),
	path('agree-to-permissions', threeleggedauth1, name="threeleggedauth1"),
	re_path(r'posting-approved$', threeleggedauth2, name="threeleggedauth2")
]