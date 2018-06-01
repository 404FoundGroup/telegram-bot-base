import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# example) SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
 }

# example) MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django_test',
#         'USER': 'django@localhost',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

INSTALLED_APPS = (
    'data',
    'bot',
)

SECRET_KEY = 'y$(e)20f4(ns*quks5%w0lg-vt5@c)o0p3k*h_%fd*4lnw-(1^'
