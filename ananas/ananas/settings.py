"""
Django settings for ananas project.
#
Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xu!k68q$@_*82ja*jgqqv+3)5o(s+gsi()cf47e-^75)sr*dv_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ananas.min.epf.fr','localhost','127.0.0.1']

PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION="FR"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'login',
    'messenger',
    'timeline',
    'phonenumber_field',
    'rest_framework',
    'rest_framework.authtoken',
    'profil',
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

ROOT_URLCONF = 'ananas.urls'

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'ananas.wsgi.application'

ASGI_APPLICATION='ananas.routing.application'

CHANNEL_LAYERS={
    'default':{
        'BACKEND':'channels_redis.core.RedisChannelLayer',
        'config':{
            'hosts':[('127.0.0.1',6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if os.name=='nt':

    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:

    DATABASES={
        'default':{
        'ENGINE':'django.db.backends.mysql',
        'OPTIONS':{
           'read_default_file':'/etc/mysql/conf.d/mysql.cnf'
          }

        }
    }


REST_FRAMEWORK={
    'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES':('rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',),
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'fr'

AUTH_USER_MODEL="login.CustomUser"

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL='/media/'

DEFAULT_FROM_EMAIL="webmaster@localhost"

#AUTH_USER_MODEL="login.CustomUser"
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
LOGIN_URL="connexion"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ananas.webmaster@gmail.com'
EMAIL_HOST_PASSWORD = 'afdauqweelyrpnph'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Ananas Team <noreply@codingwithmitch.com>'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT="/var/www/ananas.min.epf.fr/production/static"
