from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('creator/', views.creator),
    path('login/', views.login),
    path('register/', views.register)
]