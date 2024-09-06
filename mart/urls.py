from django.urls import path
from . import views

app_name = 'mart'
urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('welcome/', views.welcome, name='welcome'),
    path('products/', views.display_products, name='display_products'),
    path('cart/', views.cart, name='cart'),  
]