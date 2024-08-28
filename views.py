from django.shortcuts import render
import csv
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
  return render(request, 'home.html')

@csrf_exempt
def track_orders(request):
  file_path ="/home/abougabal/PycharmProjects/Django/ecommerce/tracking_system/dummy_orders.csv"
  if request.method == 'GET':
    with open(file_path,mode='r') as csvfile:
      reader = csv.DictReader(csvfile)
      orders = list(reader)
    return JsonResponse({'orders':orders},safe=False)
  elif request.method == 'POST':
    new_order = request.POST
    with open(file_path,mode='a',newline='') as file:
      fieldnames = ['OrderID', 'OrderName', 'Username', 'Status']
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writerow({
        'OrderID': new_order['OrderID'],
        'OrderName': new_order['OrderName'],
        'Username': new_order['Username'],
        'Status': new_order['Status']
      })
      return HttpResponse(status=201)



