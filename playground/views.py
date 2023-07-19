from django.core.cache import cache
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from store.models import Product
from rest_framework.views import APIView
from .tasks import notify_customers
import logging
import requests

# Create your views here.
logger = logging.getLogger(__name__)

class LggingClass(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'Mosh'})


class ClassBasedCache(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': data})


@cache_page(5 * 60)
def function_based_cache(request):
    response = requests.get('https://httpbin.org/delay/2')
    data = response.json()
    return render(request, 'hello.html', {'name': data})


def say_hello(request):
    queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)


    return render(request, 'hello.html', {'name': 'Samuel', 'products': list(queryset)})


def send_mail_to_customer(request):
    try:
        send_mail('subject', 'message', 'info@sammybuy.com',['sam@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Samuel'})


def send_mail_to_admins(request):
    try:
        mail_admins('subject', 'message', html_message='message')
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Admin'})




def send_mail_with_file_attached(request):
    try:
        message = EmailMessage('subject', 'message', 'info@sammybuy.com',['sam@gmail.com'])
        message.attach_file('playground/static/images/slattery.jpg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Attached File'})


def notify_project_customers(request):
    notify_customers.delay('hello')
    return render(request, 'hello.html', {'name': 'Celery File'})


def slow_api(request):
    requests.get('https://httpbin.org/delay/2')
    return render(request, 'hello.html', {'name': 'Simulating a slow api'})

def low_level_cache_api(request):
    key = 'httpbin_result'
    if cache.get(key) is None:
        response =  requests.get('https://httpbin.org/delay/2')
        data = response.json()
        cache.set(key,data)
    return render(request, 'hello.html', {'name': cache.get(key)})


