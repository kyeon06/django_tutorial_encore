from django.views.generic.base import TemplateView
# 새로운 레코드 생성을 위한 폼 뷰 보임, 테이블 레코드 생성
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.contrib.auth.mixins import AccessMixin

class UserCreateView(CreateView):
    # forms.py에 정의 되어 있는 form 클래스
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    
    # 폼에 입력 된 내용에 에러가 없고, 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정
    # url 패턴 전달인자, urls.py 모듈이 메모리 로딩된 후에 실행
    # 위의 내용이 성공했으면 아래의 문장 실행
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


# 로그인한 사용자가 콘텐츠의 소유자 인지 판별
# 소유자면 정상처리, 소유자가 아닌 경우 이 속성이 true -> 403 처리/ false -> 로그인 페이지로 이동
# 403 응답 시 보여줄 메세지를 지정
class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs):
        # 대상이 되는 객체 가져오기
        obj = self.get_object()

        # 현재 사용자와 글 소유자가 같은지 판단
        if request.user != obj.owner:
            # 다르면 403 exception 처리
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)