from django.shortcuts import render

# Create your views here.
def dashBoard(request):
    return render(request, 'dashboard/dashboard.html')