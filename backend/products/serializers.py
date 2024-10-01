from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import hello_not_allow_in_title, unique_product_title, validateTitle
from drf_api.serializers import UserPublicSerializer


class ProductInLineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    # related_products = ProductInLineSerializer(source='user.product_set.all', read_only=True, many=True)
    # my_user_data = serializers.SerializerMethodField()
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # update_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    title = serializers.CharField(validators=[validateTitle, hello_not_allow_in_title, unique_product_title]) #External validators
    # name = serializers.CharField(source='title', read_only=True)
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'id',
            'title',
            'content',
            'price',
            'image',
            'sale_price',
            'public'
        ]

    # def get_my_user_data(self, obj):
    #     return {
    #         'username': obj.user.username
    #     }

    # Inline validators
    # def validate_title(self, value):
    #     # print(self.context)
    #     # request = self.context.get('request')
    #     # user = request.user
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def get_update_url(self, obj):
    #     # return f"/product/veiwsets/{obj.pk}/"
    #     request = self.context.get('request') # self.request
    #     if request is None:
    #         return None
    #     return reverse('product-update', kwargs={'pk': obj.pk}, request=request)


    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()

        