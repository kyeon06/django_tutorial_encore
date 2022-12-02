from django.contrib import admin
from django.urls import path, include
from community.views import indexPage
from .views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    # 관리자 페이지 url
    path('admin/', admin.site.urls),
    
    path('', indexPage, name='index'),
    path('community/', include('community.urls')),
    path('dashboard/', include('dashboard.urls')),
    
    
    # django.contrib.auth.urls 장고 내장 인증 urls 활용
    path('accounts/', include('django.contrib.auth.urls')),
    # login 인증 path
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    # 계정 생성이 완료 됐다는 메세지를 보여줌
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done')
]
