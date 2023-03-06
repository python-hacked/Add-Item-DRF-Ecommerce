from rest_framework import viewsets
from product_api.models import *
from product_api.serializers import *
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [permissions.IsAuthenticated]