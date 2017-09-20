# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
# The SECRET_KEY is provided via an environment variable in OpenShift
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    # safe value used for development when DJANGO_SECRET_KEY might not be set
    '9e4@&tw46$l31)zrqe3wi+-slqm(ruvz&se0^%9#6(_w3ui!c0'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'welcome',
    'direcciones',
)

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {  # Motor de Templates Jinja =============================================
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            '%s/templates/' % (PROJECT_DIR),
            'direcciones/templates/',
            'welcome/templates/'
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'project.jinja.env.JinjaEnvironment',
            'extensions': [
                    'jdj_tags.extensions.DjangoCompat',
                    'jinja2.ext.i18n',
                    'jinja2.ext.with_',
                    'jinja2.ext.autoescape'
                ]
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '%s/templates/' % (PROJECT_DIR),
            '%s/templates/registration/' % (PROJECT_DIR)
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                # add this processor
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
from . import database
DATABASES = {'default': database.config()}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/--------------------------
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'es-MX'

ugettext = lambda s: s  # Funcion simuladora
#Lenguaje preferido por el usuario actual
LANGUAGES = (
    ('es', ugettext('Spanish')),
    ('en', ugettext('English')),
)

# Definimos la ruta de los archivos de idiomas
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

TIME_ZONE = 'America/Mexico_City'
USE_TZ = True
#------------------------------------------------------------------------------


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'