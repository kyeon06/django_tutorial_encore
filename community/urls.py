from django.contrib import admin
from django.urls import path
from community.views import WriteFormView, ArticleListView, ArticleDetailView, ArticleChangeView, ArticleUpdateView, ArticleDeleteView

app_name = 'community'
urlpatterns = [
    # write
    # path('write/', write, name='write'),
    path('write/', WriteFormView.as_view(), name='write'),

    # list
    # path('list/', articleList, name='list'),
    path('list/', ArticleListView.as_view(), name='list'),

    # view_detail
    # path('view_detail/<int:num>/', viewDetail, name='view_detail'),
    path('view_detail/<slug:pk>/', ArticleDetailView.as_view(), name='view_detail'),

    # change : login user 리스트 확인
    path('change/', ArticleChangeView.as_view(), name='change_list'),

    # update
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='update'),

    # delete
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),

]
