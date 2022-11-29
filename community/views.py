from django.shortcuts import render
from .forms import Form
from .models import Article
# Create your views here.

def write(request):
    # request가 post이면
    # 사용자가 입력한 데이터를 변수에 저장
    # ORM으로 DB에 저장
    if request.method == 'POST':

        form = Form(request.POST)
        # 데이터가 있는지 없는지 있으면 DB에 저장 
        if form.is_valid():
            form.save()
    # request가 post가 아니면
    else:
        form = Form() # Form 객체 생성
    data = "정보를 입력하세요."
    return render(request, 'write.html', {'data':data, 'form':form})


def articleList(request):
    # Article객체에 들어있는 필드 객체 모두를 불러온다.
    article_list = Article.objects.all()
    return render(request, 'list.html', {'article_list':article_list})


def viewDetail(request, num=1):
    # 클릭한 레코드를 읽어온다.
    article_detail = Article.objects.get(id=num)
    return render(request, 'view_detail.html', {'article_detail':article_detail})
