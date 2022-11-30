from django.urls import path
from dashboard.views import dashBoard

app_name = 'dashboard'
urlpatterns = [
    path('', dashBoard, name='dashboard'),
]
