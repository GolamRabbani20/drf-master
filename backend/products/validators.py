# validator is useful for namy context, It not just for DRF but also you can create validators directly for model or model form. In this case i'm going just validate this title and use it only for rest-framework

from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

# Is already a product name?
def validateTitle(value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value 

# hello is not allow as a product name.
def hello_not_allow_in_title(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError(f"{value} is not allow as a product name.")
    return value

# This field must be unique.
unique_product_title = UniqueValidator(queryset=Product.objects.all())