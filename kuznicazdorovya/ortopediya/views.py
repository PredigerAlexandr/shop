from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


menu = [{'title': "Главная", "url_name": 'home'},
{'title': "Каталог", "url_name": 'catalog'},
{'title': "Магазины", "url_name": 'stores', 'another': [{'title':'Радищева', 'id':1}, {'title':'Нариманова', 'id':2},
                                                        {'title':'Богдана-Хмельницкого', 'id':3}, {'title':'Кирова','id':4}]},
{'title': "О нас", "url_name": 'about'}
]
date = datetime.now()
def index(request):
    context = {
        'menu':menu,
        'date':date
    }
    return render(request, 'ortopediya/index.html', context = context)

def about(request):
    context = {
        'menu': menu,
        'date': date
    }
    return render(request,'ortopediya/about.html', context=context)

def show_store(request, id_store):
    context = {
        'menu': menu,
        'date': date,
        'id_store': id_store,
    }
    return render(request, 'ortopediya/store.html', context=context)


def catalog(request):
    context = {
        'menu': menu,
        'date': date
    }
    return render(request, 'ortopediya/catalog.html', context=context)