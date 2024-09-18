from django.shortcuts import render, HttpResponse

# Create your views here.
def api_home(request, *agrs, **kwargs):
    return HttpResponse('Allhumdulillah! I am from api home!')