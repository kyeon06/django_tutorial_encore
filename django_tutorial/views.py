from django.views.generic.base import TemplateView
# 새로운 레코드 생성을 위한 폼 뷰 보임, 테이블 레코드 생성
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateUserForm

class UserCreateView(CreateView):
    # forms.py에 정의 되어 있는 form 클래스
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    
    # 폼에 입력 된 내용에 에러가 없고, 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정
    # url 패턴 전달인자, urls.py 모듈이 메모리 로딩된 후에 실행
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'