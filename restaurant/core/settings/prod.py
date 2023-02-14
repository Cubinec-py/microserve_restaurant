from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGDATABASE'),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'HOST': os.environ.get('PGHOST'),
        'PORT': os.environ.get('PGPORT'),
    }
}

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

password = os.environ.get('PASSWORD_REDIS')
CELERY_TIMEZONE = "Europe/Kiev"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = f'redis://default:{password}@redis-10048.c250.eu-central-1-1.ec2.cloud.redislabs.com:10048'
CELERY_BROKER_URL = f'redis://default:{password}@redis-10048.c250.eu-central-1-1.ec2.cloud.redislabs.com:10048'

CSRF_TRUSTED_ORIGINS = ['https://microserverestaurant-production.up.railway.app']
