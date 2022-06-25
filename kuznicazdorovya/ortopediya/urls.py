from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('store/<int:id_store>', show_store, name='store'),
    path('about/', about, name='about')
]