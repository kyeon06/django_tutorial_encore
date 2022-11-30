from django.contrib import admin
from django.urls import path, include
from community.views import indexPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', indexPage, name='index'),
    path('community/', include('community.urls')),
    path('dashboard/', include('dashboard.urls')),
]
