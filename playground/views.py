from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product


# Create your views here.

def say_hello(request):
    queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    return render(request, 'hello.html', {'name': 'Samuel', 'products': list(queryset)})
