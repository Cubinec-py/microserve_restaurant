from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'DB_NAME': 'django_db',
        'DB_USER': 'y2xlxdiifbs7jfwxc3z4',
        'DB_PASSWORD': os.environ.get('DB_PASSWORD'),
        'DB_HOST': 'eu - west.connect.psdb.cloud',
        'DB_PORT': '3306',
        'MYSQL_ATTR_SSL_CA': '/ etc / ssl / cert.pem',
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
