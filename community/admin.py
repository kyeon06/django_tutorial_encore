from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('제목', {'fields':['title']}),
        ('내용', {'fields':['contents']}),
        ('작성자 정보', {'fields':['name','url','email']}),
        ('작성자 id', {'fields':['owner'], 'classes':['collapse']}),
    ]

    list_display = ('pk','title','url','cdate')
    
    #필터 추가
    list_filter = ['cdate']
    search_fields = ['title', 'contents']


# admin 페이지에 Article 데이터 모델 등록
# 이렇게 하면 관리 페이지에서 데이터 CRUD를 할 수 있게 된다.
admin.site.register(Article, ArticleAdmin)