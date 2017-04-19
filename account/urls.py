from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login

from account import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
]