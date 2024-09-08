from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    # active products from the database and then we do serialize!!
    active_products = Product.objects.filter(active=True)
    serializer = ProductSerializer(active_products, many=True)
    # Return the serialized complex data as JSON to be dealt with easily :D
    return Response(serializer.data)
