#archivo setings para trabajar en produccion
#archivo settings para trabajar localmente

from .base import *
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#configuramos db de postgresql
DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER' : 'user',
        'PASSWORD' : '.',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]#directorio para reconocer la carpeta con archivos staticos
STATIC_ROOT = BASE_DIR.child('staticfiles') #conf para sv,  staticos para prod


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')