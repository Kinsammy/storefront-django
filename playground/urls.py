from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('customer/', views.send_mail_to_customer),
    path('admin-mail/', views.send_mail_to_admins),
    path('attached-file/', views.send_mail_with_file_attached),
]