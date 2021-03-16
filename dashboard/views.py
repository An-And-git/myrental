from django.shortcuts import render
from .models import Dashboard
# Create your views here.

def home(request):
    dashboard = Dashboard.objects
    return render(request, 'home/dashboard.html', {'dashboard':dashboard})

def test(request):
    context = {
        "data": [1, 2, 3, 4, 5, 6, 7, 8],
    }
    return render(request, 'home/dashboard.html', {'dashboard':dashboard})