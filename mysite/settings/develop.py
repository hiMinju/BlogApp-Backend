from .base import *


SECRET_KEY = 'django-insecure-cgmr1q&dn@2%o-a12_%(8(c0i@qpw*1@xa!lqp-8k3c54r4acv'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}