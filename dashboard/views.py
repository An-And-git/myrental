from django.shortcuts import render
from .models import Dashboard
# Create your views here.

def home(request):
    dashboard = Dashboard.objects
    return render(request, 'home/dashboard.html', {'dashboard':dashboard})