# -*- coding: utf-8 -*-

"""
Django settings for sgo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# points to correct documents directory

SERVER_URL = ''
#SERVER_URL = '/sgo_teste'
#SERVER_URL = '/sgo'

TEMPLATE_DIRS = [ os.path.join(BASE_DIR, 'templates'),

                ]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOCAL = True

if SERVER_URL == '/sgo':
    MEDIA_ROOT = '/home/inventsis/www/docs'
else:
    MEDIA_ROOT = '/home/inventsis/www/docs_teste'

if DEBUG:
    MEDIA_URL = 'http://127.0.0.1:8000/docs/'
else:
    if SERVER_URL == '/sgo':
        MEDIA_URL = 'http://www.inventsis.com.br/docs/'
    else:
        MEDIA_URL = 'http://www.inventsis.com.br/docs_teste/'

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),#Files Source
    )
    STATIC_ROOT= os.path.join(BASE_DIR,'')
    STATIC_URL = '/static/'
else:
    STATICFILES_DIRS = ( #Where Django looks for the collect static command
        os.path.join(PROJECT_ROOT, 'static'),
    )
    STATIC_ROOT= os.path.join(BASE_DIR,'static') #Django uses to collect all static files from "STATICFILES_DIRS"
    STATIC_URL = SERVER_URL+'/static/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']


TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'logentry',
	'pedido',
    'cliente',
    'grade',
    'multa',
    'falta',
    # 'produto',
    # 'transportadora',
    # 'estabelecimento',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sgo.urls'

WSGI_APPLICATION = 'sgo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOCALE_PATHS = ('/locale', )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    #"report.context_processors.server_url",
    "django.template.context_processors.request",
)
