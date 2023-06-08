
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from store.models import Product
from .tasks import notify_customers

# Create your views here.

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


