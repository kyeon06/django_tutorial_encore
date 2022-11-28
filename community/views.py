from django.shortcuts import render

# Create your views here.

def write(request):
    # 비즈니스로직
    # data = {'key' : 'value'}
    # render(request, template.html, data)

    hello = "hello django"
    hello2 = "알고보니 쉬운 django"
    return render(request, 'write.html', {'data' : hello, 'data1' : hello2})
    # 해당 html파일에 data를 실어서 respone 해주겠다는 문장.