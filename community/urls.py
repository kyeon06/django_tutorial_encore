from django.contrib import admin
from django.urls import path
from community.views import WriteFormView, ArticleListView, ArticleDetailView

app_name = 'community'
urlpatterns = [
    # path('write/', write, name='write'),
    path('write/', WriteFormView.as_view(), name='write'),

    # path('list/', articleList, name='list'),
    path('list/', ArticleListView.as_view(), name='list'),
    
    # path('view_detail/<int:num>/', viewDetail, name='view_detail'),
    path('view_detail/<slug:pk>/', ArticleDetailView.as_view(), name='view_detail'),
]
