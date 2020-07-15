import os

from configurations import Configuration, values

from .base import Base


class Development(Base, Configuration):
    DEBUG = values.BooleanValue(True)
    BASE_DIR = Base.BASE_DIR
    SECRET_KEY = values.SecretValue()
    ALLOWED_HOSTS = ["*"]

    # DJANGO CHANNELS
    ASGI_APPLICATION = "config.routing.application"
    CHANNEL_LAYERS = {
        'default': {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [(os.getenv('REDIS_URL'), 6379)],
            },
        }
    }

    # HAYSTACK CONFIGURATION
    HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
            'URL': os.getenv('ELASTICSEARCH_URL'),
            'INDEX_NAME': 'haystack',
        },
    }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "postgres",
            'USER': "postgres",
            'PASSWORD': "postgres",
            'HOST': "0.0.0.0",
            'PORT': 5432
        }
    }