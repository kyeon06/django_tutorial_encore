from django.shortcuts import render
from .forms import Form
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