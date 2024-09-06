# mart/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import urlencode
from Products.models import Product  # Import the Product model

def index(request):
    products = {"sunglasses": 500, "microwave": 700, "tshirt": 230}
    if request.method == "POST":
        selected_products = request.POST.getlist('products')
        query_string = urlencode({'options': selected_products})
        return redirect(f'/cart/?{query_string}')

    return render(request, 'mart/index.html', {'products': products})

def show(request):
    selected_products = request.GET.getlist('options')
    return HttpResponse(f'Selected products: {selected_products}')

def welcome(request):
    return HttpResponse("Welcome to the Mart!")

def display_products(request):
    active_products = Product.objects.filter(isActive=True)
    return render(request, 'mart/products.html', {'products': active_products})

def cart(request):
    selected_products = request.GET.getlist('products')
    products = {
        "sunglasses": 500,
        "microwave": 700,
        "tshirt": 230,
    }
    cart_products = []
    total = 0
    for product in selected_products:
        if product in products:
            cart_products.append({
                'name': product,
                'price': products[product],
            })
            total += products[product]
    return render(request, 'mart/cart.html', {'products': cart_products, 'total': total})