# mart/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('welcome/', views.welcome, name='welcome'),
    path('products/', views.display_products, name='display_products'),
]