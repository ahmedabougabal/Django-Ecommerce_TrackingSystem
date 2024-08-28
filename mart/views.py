from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import urlencode


def index(request):
  products = {"sunglasses": 500, "microwave": 700, "tshirt": 230}
  if request.method == "POST":
    selected_products = request.POST.getlist('products')
    query_string = urlencode({'options': selected_products})
    return redirect(f'/cart/?{query_string}')

  return render(request, 'mart/index.html', {'products': products})


def cart(request):
  selected_products = request.GET.getlist('options')
  return HttpResponse(f'Selected products: {selected_products}')
