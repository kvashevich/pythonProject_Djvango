from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def show_main(request):
    return render(request, 'main/layout.html')


def show_cats(request):
    return render(request, 'main/cats.html')


def show_dogs(request):
    return render(request, 'main/dogs.html')


def show_birds(request):
    return render(request, 'main/birds.html')
