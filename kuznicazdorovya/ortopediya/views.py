from django.http import HttpResponse
from django.shortcuts import render


menu = [{'title': "Главная", "url_name": 'home'},
{'title': "Каталог", "url_name": 'catalog'},
{'title': "Магазины", "url_name": 'stores'},
{'title': "О нас", "url_name": 'about'}
]

def index(request):
    context = {
        'menu':menu
    }
    return render(request, 'ortopediya/base.html', context = context)

def about(request):
    return HttpResponse('О нас')

def show_stores(request):
    return HttpResponse('Магазины')

def catalog(request):
    return HttpResponse('Каталог')