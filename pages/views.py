from django.shortcuts import render
from .models import Team
# Create your views here.

def home(request):
    data = {'teams':Team.objects.all()}
    return render(request,'pages/home.html',data)

def about(request):
    data = {'teams':Team.objects.all()}
    return render(request,'pages/about.html',data)

def contact(request):
    return render(request,'pages/contact.html')

def cars(request):
    return render(request,'pages/cars.html')

def services(request):
    return render(request,'pages/services.html')
