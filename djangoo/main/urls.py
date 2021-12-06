from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main, name='main'),
    path('cats/', views.show_cats, name='cats'),
    path('dogs/', views.show_dogs, name='dogs'),
    path('birds/', views.show_birds, name='birds'),
]
