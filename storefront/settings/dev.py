from .common import *

DEBUG = True
SECRET_KEY = env("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
    }
}