from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def home(request):
    return render(request, 'base/home.html')
def creator(request):
    return render(request, 'base/creator.html')

def login(request):
    return render(request, 'base/login.html')

def register(request):
    return render(request, 'base/register.html')