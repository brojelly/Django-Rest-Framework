# config/settings/local.py
from .base import *


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': secret["DB_NAME"],
        'USER': secret["DB_USER"],
        'PASSWORD': secret["DB_PASSWORD"],
        'HOST': secret["DB_HOST"],
        'PORT': secret["DB_PORT"],
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']