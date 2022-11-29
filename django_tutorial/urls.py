"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from community.views import write, articleList, viewDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', write, name='write'),
    path('list/', articleList, name='list'),
    # / 없으면 안되고 변수를 지정할 경우 <> 안에 넣는다.
    # num이 viewDetail로 넘어가서 해당 id에 글을 보여준다.
    path('view_detail/<int:num>/', viewDetail, name='view_detail'),
]
