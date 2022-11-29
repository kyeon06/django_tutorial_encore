from django.contrib import admin

# Register your models here.

from .models import Article

# admin 페이지에 Article 데이터 모델 등록
# 이렇게 하면 관리 페이지에서 데이터 CRUD를 할 수 있게 된다.
admin.site.register(Article)