from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .models import *

stores = Store.objects.all()
menu = [{'title': "Главная", "url_name": 'home'},
        {'title': "Каталог", "url_name": 'catalog'},
        {'title': "Магазины", "url_name": 'stores', 'another': stores},
        {'title': "О нас", "url_name": 'about'}
        ]
date = datetime.now()


def index(request):
    index_products = Index_product.objects.all()
    for i in index_products:
        p = i.id_product
        print(p.name)
    context = {
        'menu': menu,
        'date': date,
        'title': 'Главная',
        'index_products': index_products,
    }
    print(menu[2]['title'])
    return render(request, 'ortopediya/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'date': date,
        'title': 'О нас',
    }
    return render(request, 'ortopediya/about.html', context=context)


def show_store(request, id_store):
    store = Store.objects.get(pk=id_store)
    print(store.map)
    context = {
        'store': store,
        'menu': menu,
        'date': date,
        'id_store': id_store,
        'title': 'Cалон на ' + store.street,
    }
    return render(request, 'ortopediya/store.html', context=context)


def catalog(request, id_cat=0):
    categories = Category.objects.all()
    if id_cat == 0:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(subcategory_id=id_cat)
    for cat in categories:
        for sub in cat.subcategory_set.all():
            print(sub)
    request.session['id_cat'] = id_cat
    context = {
        'products': products,
        'categories': categories,
        'menu': menu,
        'date': date,
        'title': 'Каталог',
    }
    return render(request, 'ortopediya/catalog.html', context=context)


def show_product(request, id_product):
    product = Product.objects.get(id=id_product)
    context = {
        'stores': stores,
        'id_cat_for_catalog_url': request.session['id_cat'],
        'product': product,
        'menu': menu,
        'date': date,
        'title': 'Продукт',
    }
    return render(request, 'ortopediya/product.html', context=context)


def show_article(request, article_name):
    if article_name == 'Биологически активные точки':
        context = {
            'stores': stores,
            'menu': menu,
            'date': date,
            'title': 'Биологически активные точки',
        }
        return render(request, 'ortopediya/article_active_tods.html', context=context)

    if article_name == 'Полезные свойства соляных ламп':
        context = {
            'stores': stores,
            'menu': menu,
            'date': date,
            'title': 'Полезные свойства соляных ламп',
        }
        return render(request, 'ortopediya/article_salt_lamps.html', context=context)