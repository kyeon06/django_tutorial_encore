from django.shortcuts import render, redirect
from .models import CountryData
from .forms import CountryDataForm

def dashBoard(request):
    if request.method == 'POST':
        
        form = CountryDataForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
  
    else:
        form = CountryDataForm()

    country_data = CountryData.objects.all()
    return render(request, 'dashboard/dashboard.html', {'dataset' : country_data, 'form': form})