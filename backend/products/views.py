from rest_framework  import generics, mixins
from .models import Product
from .serializers import ProductSerializer

# function based view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from django.http import Http404
from drf_api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Details view
class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView, UserQuerySetMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
product_detail_view = ProductDetailAPIView.as_view()

# List and Create both in one method
class ProductListCreateAPIView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        
    # Replaced by mixin
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user=request.user
    #     # print(dir(request))
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=user)
    
product_list_create_view = ProductListCreateAPIView.as_view()

# Function based view
@api_view(['POST', 'GET'])
def Products_all_Views(request, pk=None, *args, **kwarg):
    method = request.method
    if method == 'GET':
        # Product Details view
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        
        # Product List view
        queryset = Product.objects.all()
        data  = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        # Create an item 
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'Invalid': 'Not goot data'}, status=404)

#------------------------------------------------------------------------------>| Destroy & Update |<---------------------------------------------------------------------------------
# Delete API View
class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView, UserQuerySetMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
product_delete_view = ProductDestroyAPIView.as_view()

# Update API View
class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView, UserQuerySetMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
   
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
    
product_update_view = ProductUpdateAPIView.as_view()

#---------------------------------------------------------------------------->|Mixins and a Generic API View |<----------------------------------------------------------------------

class ProductMixinView(mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

    # List and Detail
    def get(self, request, *args, **kwargs): # HTTP -> get
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    # Create
    def post(self, request, *args, **kwargs): # HTTP -> post
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title + 'Hi, I am from create mixin'
        serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()







