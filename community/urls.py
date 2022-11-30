from django.contrib import admin
from django.urls import path
from community.views import write, articleList, viewDetail

app_name = 'community'
urlpatterns = [
    path('write/', write, name='write'),
    path('list/', articleList, name='list'),
    path('view_detail/<int:num>/', viewDetail, name='view_detail'),
]
