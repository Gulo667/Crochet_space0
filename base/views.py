from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from .models import *

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def creator(request):
    return render(request, 'base/creator.html')

def login(request):
    return render(request, 'base/login.html')

def register(request):
    return render(request, 'base/register.html')

def store(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'base/store.html', context)

def cart(request):
    context = {}
    return render(request, 'base/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'base/checkout.html', context) 