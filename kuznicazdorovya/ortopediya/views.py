from django.http import HttpResponse
from django.shortcuts import render


menu = [{'title': "Главная", "url_name": 'home'},
{'title': "Каталог", "url_name": 'catalog'},
{'title': "Магазины", "url_name": 'stores', 'another': [{'title':'Радищева', 'id':1}, {'title':'Нариманова', 'id':2},
                                                        {'title':'Богдана-Хмельницкого', 'id':3}, {'title':'Кирова','id':4}]},
{'title': "О нас", "url_name": 'about'}
]

def index(request):
    context = {
        'menu':menu
    }
    return render(request, 'ortopediya/base.html', context = context)

def about(request):
    return HttpResponse('О нас')

def show_store(request, id_store):
    return HttpResponse(f'Магазины {id_store}')

def catalog(request):
    return HttpResponse('Каталог')