from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('catalog/<int:id_cat>', catalog, name='catalog'),
    path('store/<int:id_store>', show_store, name='store'),
    path('about/', about, name='about'),
    path('catalog/product/<int:id_product>', show_product, name='product'),
    path('article/<str:article_name>', show_article, name='article'),
]