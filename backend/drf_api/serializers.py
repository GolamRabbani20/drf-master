from rest_framework import serializers


class UserProductInLineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    # email = serializers.EmailField(read_only=True)

    # other_products = serializers.SerializerMethodField(read_only=True)
    # def get_other_products(self, obj):
    #     user = obj
    #     my_products_qs = user.product_set.all()
    #     return UserProductInLineSerializer(my_products_qs, many=True).data
