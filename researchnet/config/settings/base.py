"""
Django settings for researchnet project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!dfk(&=25el=cf!=tzm2m4q+ym8#f-c7=q_r)7#b1#!_%gokw@'


ALLOWED_HOSTS = []



# Application definition
INSTALLED_APPS = (
    
    # Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Vendor
    'djangobower',
    'compressor',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',

    # Mine
    'dashboard',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
            }
    }
]

WSGI_APPLICATION = 'config.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)

BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components')

BOWER_INSTALLED_APPS = (
    'jquery#2.1.4',
    'd3#3.5.6',
    'moment#2.10.6',
    'foundation#5.5.2',
    'font-awesome#4.4.0',
    'dcjs#1.7.5',
)

REST_FRAMEWORK = {
    'PAGE_SIZE': 20,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}




# We recommend https://www.sparkpost.com
if 'EMAIL_HOST' in os.environ:
    EMAIL_HOST = os.environ['EMAIL_HOST'] 

if 'EMAIL_HOST_USER' in os.environ:
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']

if 'EMAIL_HOST_PASSWORD' in os.environ:  
    EMAIL_HOST_PASSWORD =  os.environ['EMAIL_HOST_PASSWORD']

if  'EMAIL_PORT' in os.environ:
    EMAIL_PORT =  os.environ['EMAIL_PORT']

if 'EMAIL_USE_TLS' in os.environ:
    EMAIL_USE_TLS =  os.environ['EMAIL_USE_TLS']

DEFAULT_FROM_EMAIL = 'researchnet@ictedge.org'
EMAIL_REGISTRATION_SUBJECT = 'Welcome to RTI\'s Researchnet'

