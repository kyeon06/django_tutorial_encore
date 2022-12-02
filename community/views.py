from .models import Article
from django.urls import reverse_lazy
# LoginRequiredMixin : 사용자가 로그인 된 경우 정상처리/로그인 안된 사용자는 로그인 페이지로 리다이렉션
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

# 작성
class WriteFormView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['name', 'title', 'contents', 'url', 'email']
    template_name = 'community/write.html'
    success_url = reverse_lazy('community:list')
    
    def form_valid(self, form):
        # 폼에 연결된 모델 객체의 owner 필드에 현재 로그인 된 user 객체 저장
        form.instance.owner = self.request.user
        return super().form_valid(form)

# 전체 목록
class ArticleListView(ListView):
    model = Article
    template_name = 'community/list.html'

# 세부사항
class ArticleDetailView(DetailView):
    model = Article
    print(DetailView.get_context_object_name)
    template_name = 'community/view_detail.html'


# 변경(login user 자료만 list_up)
class ArticleChangeView(LoginRequiredMixin, ListView):
    template_name = 'community/change_list.html'

    # login된 user의 자료만 불러오는 query
    # 화면에 출력할 레코드 리스트 반환
    def get_queryset(self):
        return Article.objects.filter(owner=self.request.user)

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

# 로그인 user 글 수정(update)
class ArticleUpdateView(OwnerOnlyMixin,UpdateView):
    model = Article
    template_name = "community/article_update.html"
    fields = ['name', 'title', 'contents','url', 'email']
    success_url = reverse_lazy('community:change_list')
 
# 로그인 user 글 삭제(delete)
class ArticleDeleteView(OwnerOnlyMixin, DeleteView):
    model = Article
    template_name = "community/article_delete.html"
    success_url = reverse_lazy('community:change_list')


#FBV
from django.shortcuts import render, redirect
from .forms import Form

def write(request):
    # request가 post이면
    # 사용자가 입력한 데이터를 변수에 저장
    # ORM으로 DB에 저장
    if request.method == 'POST':

        form = Form(request.POST)
        # 데이터가 있는지 없는지 있으면 DB에 저장 
        if form.is_valid():
            form.save()
            return redirect('/community/list')
    # request가 post가 아니면
    else:
        form = Form() # Form 객체 생성
    data = "정보를 입력하세요."
    return render(request, 'community/write.html', {'data':data, 'form':form})


def articleList(request):
    # Article객체에 들어있는 필드 객체 모두를 불러온다.
    article_list = Article.objects.all().order_by('-cdate')
    return render(request, 'community/list.html', {'article_list':article_list})


def viewDetail(request, num=1):
    # 클릭한 레코드를 읽어온다.
    article_detail = Article.objects.get(id=num)
    return render(request, 'community/view_detail.html', {'article_detail':article_detail})

def indexPage(request):
    index_page = Article.objects.all().order_by('-cdate')[:3]
    return render(request, 'index.html', {'index_page':index_page})