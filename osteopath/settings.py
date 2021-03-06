"""
Django settings for osteopath project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['osteosport.org','localhost', '127.0.0.1','https://osteosport.herokuapp.com/']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    "crispy_bootstrap5",
    'bootstrap5',
    'accounts',
    'visitors',
    'staff',
    'appointment',
    'captcha',
    'social_django',
    'django_extensions',
    'storages',
    'ckeditor',
    'django_celery_beat',
    'django_celery_results',
    'celery',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'osteopath.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

WSGI_APPLICATION = 'osteopath.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
import os

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR/'staticfiles'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')





# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = 'about'
LOGIN_REDIRECT_URL = 'about'

AUTHENTICATION_BACKENDS =['django.contrib.auth.backends.ModelBackend',
                          'social_core.backends.facebook.FacebookOAuth2',
                          'social_core.backends.google.GoogleOAuth2']


RECAPTCHA_DOMAIN = 'www.recaptcha.net'
RECAPTCHA_REQUIRED_SCORE = 0.85

AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'eu-central-1'
AWS_S3_SIGNATURE_VERSION = 's3v4'

# CELERY SETTINGS

CELERY_BROKER_URL = 'amqp://guest@localhost//'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Jerusalem'

CELERY_RESULT_BACKEND = 'django-db'

#CELERY BEAT
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


# CELERY_BROKEN_URL = 'amqp://guest@localhost//'
# CELERY_RESULT_BACKEND = 'django-db'
# # REDIS_URL = "redis://localhost:6379"
# # CELERY_BROKER_URL=REDIS_URL
# # CELERY_RESULT_BACKEND=REDIS_URL
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Asia/Jerusalem'
# CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

import django_heroku

try:
    from.local_settings import *
except ImportError:
    django_heroku.settings(locals())
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG')
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 587
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    RECAPTCHA_PUBLIC_KEY = os.environ.get(str('RECAPTCHA_PUBLIC_KEY'))
    RECAPTCHA_PRIVATE_KEY = os.environ.get(str('RECAPTCHA_PRIVATE_KEY'))

    SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get(str('SOCIAL_AUTH_FACEBOOK_KEY'))
    SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get(str('SOCIAL_AUTH_FACEBOOK_SECRET'))

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get(str('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'))
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get(str('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'))

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_URL = os.environ.get('AWS_URL')

 #   CElERY_BROKER_URL = os.environ.get('CElERY_BROKER_URL', 'amqp://guest:guest@127.0.0.1//')

MEDIA_URL = AWS_URL + '/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# import smtplib
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.ehlo()
# server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

# import smtplib
# server = smtplib.SMTP('smtp.gmail.com', 25)
# server.connect('smtp.gmail.com', 25)