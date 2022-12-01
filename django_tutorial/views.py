from django.views.generic.base import TemplateView
from django.views.generic import CreateView # 새로운 레코드 생성을 위한 폼 뷰 보임, 테이블 레코드 생성
from django.urls import reverse_lazy
from .forms import CreateUserForm

class UserCreateView(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/register.html'

    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registeration/register_done.html'