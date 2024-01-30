from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = 'store'),
    path('creator/', views.creator, name = 'creator'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout')
]