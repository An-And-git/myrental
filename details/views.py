from django.shortcuts import render
from .models import Details
# Create your views here.

def details(request):
    details = Details.objects
    return render(request, 'details/details.html', {'details':details})
