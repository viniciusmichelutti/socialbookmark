from django.conf.urls import url
from django.contrib.auth.views import logout_then_login, LoginView

from account import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', LoginView.as_view(redirect_authenticated_user=True) , name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
]