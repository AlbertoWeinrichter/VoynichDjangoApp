import json
import os

from configurations import Configuration
from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate
from six.moves.urllib import request


class Base(Configuration):
    DEBUG = os.getenv('DEBUG')
    BASE_DIR = os.getcwd()
    SECRET_KEY = os.getenv('SECRET_KEY')

    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        'API.user',

        'rest_framework',
        'rest_framework.authtoken',
        'channels',
        'storages',
        'haystack',
        'django_nose',

        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'corsheaders',
    ]

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    AUTH_USER_MODEL = 'user.User'

    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_HEADERS = [
        'accept',
        'accept-encoding',
        'authorization',
        'content-disposition',
        'content-type',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
    ]

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'API.user.jsonwebtoken_auth_backend.JsonTokenBackend',
        )
    }
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'config.urls'

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

    WSGI_APPLICATION = 'config.wsgi.application'

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

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # S3 Storages
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    AWS_STATIC_LOCATION = 'static'
    STATIC_ROOT = BASE_DIR
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
    ADMIN_MEDIA_PREFIX = STATIC_URL

    AWS_MEDIA_LOCATION = 'media'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)

    STATICFILES_LOCATION = 'static'
    MEDIAFILES_LOCATION = 'media/'
    STATICFILES_STORAGE = 'config.storage_backends.StaticStorage'
    DEFAULT_FILE_STORAGE = 'config.storage_backends.MediaStorage'

    # This is for admin, not normal API
    AUTHENTICATION_BACKENDS = {
        'django.contrib.auth.backends.ModelBackend'
    }

    # Auth0 And JsonWebToken configuration
    AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID')
    AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')

    AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')

    jsonurl = request.urlopen('https://' + AUTH0_DOMAIN + '/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read().decode('utf-8'))
    cert = '-----BEGIN CERTIFICATE-----\n' + jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'
    certificate = load_pem_x509_certificate(cert.encode('utf-8'), default_backend())
    PUBLIC_KEY = certificate.public_key()

    BOOTSTRAP_ADMIN_SIDEBAR_MENU = False

    #  _____ _____ __    _____ _____ __ __
    # |     |   __|  |  |   __| __  |  |  |
    # |   --|   __|  |__|   __|    -|_   _|
    # |_____|_____|_____|_____|__|__| |_|
    BROKER_URL = 'amqp://{user}:{password}@{hostname}'.format(
        user=os.environ.get('RABBIT_ENV_USER', 'admin'),
        password=os.environ.get('RABBIT_ENV_RABBITMQ_PASS', 'mypass'),
        hostname=os.environ.get('RABBIT_ENV_HOST', 'rabbit'))

    BROKER_POOL_LIMIT = 1
    BROKER_CONNECTION_TIMEOUT = 10

    CELERY_DEFAULT_QUEUE = os.environ.get('APP_NAME', '')
    CELERY_ALWAYS_EAGER = False
    CELERY_ACKS_LATE = True
    CELERY_TASK_PUBLISH_RETRY = True
    CELERY_DISABLE_RATE_LIMITS = False
    CELERY_TASK_SERIALIZER = "json"
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERYD_HIJACK_ROOT_LOGGER = False
    CELERYD_PREFETCH_MULTIPLIER = 1
    CELERYD_MAX_TASKS_PER_CHILD = 1000

    CELERY_IMPORTS = ('API.example.tasks',)

    CELERYBEAT_SCHEDULE = {
        # 'quote_harvesting': {
        #     'task': 'quotes.tasks.topic_discovery',
        #     'schedule': crontab(hour="*/10"),
        #     'args': ("Hello I'm an arg",)
        # },
    }
