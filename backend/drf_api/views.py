from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwagrs):
    """ DRF API View """
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # doen't show the sale price by this method model_to_dict that is one of many reason to used serializer
        # data = model_to_dict(instance, fields=['id', 'title', 'content', 'price', 'sale_price'])
        # data['image'] = instance.image.url
        data = ProductSerializer(instance).data
    return JsonResponse(data)

# def api_home(request, *agrs, **kwargs):
#     # model instance(model_data) -> turn a python dict -> return JSON to my client = serializer
#     model_data = Product.objects.all().order_by('?').first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price']) # convert model instance -> python dict 
#         data['image'] = model_data.image.url
    #   data['id'] = model_data.id
    #   data['title'] = model_data.title
    #   data['content'] = model_data.content
    #   data['price'] = model_data.price
    #   data['image'] = model_data.image.url

    # return JsonResponse(data) # Accept a python dict
    # return HttpResponse(data, headers={"content-type": "application/json"})

    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.bady 
    # print(request.GET) # url query params
    # print(request.POST)
    # body = request.body # byte string JSON data 
    # data = {}
    # try:
    #     data = json.loads(body)  # convert byte json string -> python dict 
    # except:
    #     pass
    # print(data)
    # data['prams'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content-type'] = request.content_type

    