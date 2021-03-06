from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.views import logout_then_login, LoginView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from account import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', LoginView.as_view(redirect_authenticated_user=True) , name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^change-password/$', PasswordChangeView.as_view(), name='change_password'),
    url(r'^change-password/done$', PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password-reset/complete$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/follow/$', views.user_follow, name='user_follow'),
    url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),
]
