"""
Django settings for menugen project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import logging
import os
import sys

from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')l)x*^74kt8y76*u8sajrckjrkk(%0d*l+utio86*bcb(47)=t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'application',
    'stdimage',
    'menus',
    'testing',
)

MIDDLEWARE_CLASSES = (
    # 'menus.middleware.ResetTLSMiddleware', #TODO: Check with Kevin usage of Middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'menugen.urls'

WSGI_APPLICATION = 'menugen.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'menugen_db',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'simple'
        },
        'logfile': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.curdir, 'menugen.log'),
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'menus': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        }
    }

}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = '/srv/data/web/vhosts/default/static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "application/static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'menus/templates'),
)

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, "application/static"),
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

CACHES = {
    'memory': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'menugen',
    },
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': '/var/tmp/MenuGenCache',                                    # GNU/Linux
        'LOCATION': os.path.join(os.path.expandvars('%TMP%'), 'MenuGenCache'),  # Windows
        'MAX_ENTRIES': 50000
    },
    'memcached': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'KEY_FUNCTION': 'hashlib.md5',
        'LOCATION': [
            '127.0.0.1:11211',
        ]
    }
}

LOGIN_URL = "/sign-in"
LOGIN_REDIRECT_URL = "/"
