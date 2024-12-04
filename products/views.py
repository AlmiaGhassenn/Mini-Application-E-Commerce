from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
    @action(detail=False, methods=['get'])
    def in_stock(self, request):
         # Retrieve the 'in_stock' query parameter from the request
        in_stock = request.query_params.get('in_stock', None)
        if in_stock == 'true':
         # Filter for products with stock greater than 0
            products = Product.objects.filter(stock__gt=0)
        else:
            # Retrieve all products if no filter is applied
            products = Product.objects.all()
        # Serialize the product data
        serializer = self.get_serializer(products, many=True)
        # Return the serialized data as a JSON response
        return Response(serializer.data)
