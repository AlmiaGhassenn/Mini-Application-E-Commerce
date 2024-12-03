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
        
        in_stock = request.query_params.get('in_stock', None)
        if in_stock == 'true':
            
            products = Product.objects.filter(stock__gt=0)
        else:
            
            products = Product.objects.all()

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
