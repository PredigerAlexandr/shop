from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('/catalog/', catalog, name='catalog'),
    path('/stores/', show_stores, name='stores'),
    path('/about/', about, name='about')
]