from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewsets(viewsets.ModelViewSet):
    # get -> List -> Queryset
    # get -> retrieve -> Product Instance DEtail View
    # post -> create -> New Instance
    # put -> Update
    # patch -> Partial Update
    # delete -> destroy
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'