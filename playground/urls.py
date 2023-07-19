from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('customer/', views.send_mail_to_customer),
    path('admin-mail/', views.send_mail_to_admins),
    path('attached-file/', views.send_mail_with_file_attached),
    path('notify/', views.notify_project_customers),
    path('slow-api/', views.slow_api),
    path('cache_api/', views.low_level_cache_api),
    path('function_cache/', views.function_based_cache),
    path('class_cache/', views.ClassBasedCache.as_view()),
    path('logging/', views.LggingClass.as_view()),
]