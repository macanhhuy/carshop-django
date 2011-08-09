# Django settings for carshop project.
import logging

logger = logging.getLogger(__name__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'carshop', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306', # Set to empty string for default. Not used with sqlite3.
    }
}

#CACHE_BACKEND = 'file://./cache'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
#USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
#USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = './medias/images/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/medias/images/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

STATIC_PATH = './medias'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c4onj+ssm4e*=*)^oyd7gnsz1syiedhti15b&67@jd9yjlnix4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
'django.middleware.common.CommonMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
#'django.middleware.cache.UpdateCacheMiddleware',
#'django.middleware.cache.FetchFromCacheMiddleware',
#'django.middleware.csrf.CsrfViewMiddleware',
'django.middleware.locale.LocaleMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
#'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
'django.core.context_processors.auth',
'django.core.context_processors.request',
#'django.core.context_processors.debug',
#'django.core.context_processors.i18n',
#'django.core.context_processors.media',
#'carshop.context_processors.getLeftNavigate',
'carshop.context_processors.getTopNavigate',
'carshop.context_processors.getCartCount',
'carshop.context_processors.getUnPalCount',
)

#SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_COOKIE_AGE = 300


ROOT_URLCONF = 'carshop.urls'

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
'./templates',
)

#import os

#DMIGRATIONS_DIR = os.path.join(os.path.dirname(__file__), 'migrations')



INSTALLED_APPS = (
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.sites',
'django.contrib.messages',
'django.contrib.admin',

'carshop',
'carshop.customer',
'carshop.brand',
'carshop.order',
'carshop.product',
'carshop.cart',

'carshop.paypal.standard.ipn',

'dmigrations',
'debug_toolbar',
'rollyourown.seo',
)

AUTH_PROFILE_MODULE = 'customer.Customer'

PAYPAL_RECEIVER_EMAIL = 'xtwxfxk@gmail.com'
PAYPAL_TEST = True
PAYPAL_WPP_USER = "xtwxfxk_api1.gmail.com"
PAYPAL_WPP_PASSWORD = "8EB49GRQ8Q6GCG4V"
PAYPAL_WPP_SIGNATURE = "AKmUkXSpzyIk02Gvvi3fVluSBs3WAvhvJ3e5WlKhRgX6XYDLQFd.7xHi"



#logging.basicConfig(  
#	level = logging.DEBUG,
#	format = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',
#	filename = 'log/filelog.log',
#)


try:
    from settings_debug_toolbar import *
except ImportError, e:
    logger.error(e)
    pass
