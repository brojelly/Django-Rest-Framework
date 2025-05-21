# config/settings/prod.py

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['brojelly.pythonanywhere.com']  # 실제 배포 주소로 변경

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / '.static_root'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
