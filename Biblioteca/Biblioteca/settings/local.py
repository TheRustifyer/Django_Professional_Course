from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret_data('DB_NAME'),
        'USER': get_secret_data('DB_USER'),
        'PASSWORD' : get_secret_data('DB_PASSWORD'),
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [Path(BASE_DIR.parent, 'static/')]