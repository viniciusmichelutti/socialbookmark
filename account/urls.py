from django.conf.urls import url
from django.contrib.auth.views import logout_then_login, LoginView, PasswordChangeView, PasswordChangeDoneView

from account import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', LoginView.as_view(redirect_authenticated_user=True) , name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^change-password/$', PasswordChangeView.as_view(), name='change_password'),
    url(r'^change-password/done$', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
