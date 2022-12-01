from django.shortcuts import render, redirect
from .models import CountryData
from .forms import CountryDataForm

def dashBoard(request):
    if request.method == 'POST':
        
        form = CountryDataForm(request.POST)
        
        if form.is_valid():
            '''
            폼에 입력 값을 개별로 변수 대입
            나라이름(country)이 DB에 저장되어있는지 확인
            입력한 나라 이름이 있으면 업데이트하고 없으면 저장
            '''

            input_country = form.data.get('country', None)
            input_num = form.data.get('population', None)

            # form.save()를 하는데 중복되는 데이터는 업데이트 없으면 추가
            CountryData.objects.update_or_create(
                country = input_country,
                defaults={ 
                    'country' : input_country,
                    'population' : input_num,
                }
            )
            # form.save()
            # return redirect('/dashboard')
            return redirect('.') # 자기 자신을 불러온다.
  
    else:
        form = CountryDataForm()

    country_data = CountryData.objects.all()
    context = {
        'dataset' : country_data,
        'form': form
    }
    return render(request, 'dashboard/dashboard.html', context)