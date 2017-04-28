from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^social-auth/', include('social_django.urls', namespace='social')),
    url(r'^images/', include('images.urls')),
]
