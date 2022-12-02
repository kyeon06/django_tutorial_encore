from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True) # 자동으로 현재 날짜 삽입
    mdate = models.DateTimeField(auto_now=True)

    # on_delete = models.CASCADE : 소유자가 삭제가 되면 소유자가 작성한 글들을 모두 삭제한다.
    # blank, null =True : 빈칸과 null 허락하겠다. (안하면 오류남)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # 내부 클래스
    class Meta:
        # 관리자 페이지의 title 변경
        verbose_name_plural = '아티클 작성하기'
        # 수정한 날짜를 기준으로 정렬
        ordering = ('-mdate',)
    
    def __str__(self):
        return f"{self.title}--{self.name}--{self.cdate}"
    
    def get_absolute_url(self):
        # args=(self.id,) 문자열로 반환해줘서 path에 id값을 실어서 리턴해준다. 
        return reverse('community:view_detail', args=(self.id,))
