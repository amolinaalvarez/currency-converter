from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('nucoro.urls.urls_api', namespace='api'))
]
