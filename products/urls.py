from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Initialize the default router and register the ProductViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)), # Include all standard routes provided by the router
    path('products/in_stock/', ProductViewSet.as_view({'get': 'in_stock'})), # Custom route for the in_stock action
]
