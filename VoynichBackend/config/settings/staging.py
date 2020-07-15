from configurations import Configuration, values
from .base import Base
import os


class Staging(Base, Configuration):
    BITCORE_SERVER_TYPE = "sta"
    DEBUG = values.BooleanValue(True)
    BASE_DIR = Base.BASE_DIR
    SECRET_KEY = values.SecretValue()
    DOMAIN_NAME = os.getenv('DOMAIN_NAME')

    ALLOWED_HOSTS = [
        "127.0.0.1",
        "0.0.0.0",
        "localhost",
        "staging." + DOMAIN_NAME + ".local",
        DOMAIN_NAME + ".com"
    ]

    # WEBSOCKETS - DJANGO CHANNELS
    ASGI_APPLICATION = "config.routing.application"
    CHANNEL_LAYERS = {
        'default': {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("redis", 6379)],
            },
        }
    }

    # HAYSTACK CONFIGURATION
    HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
            'URL': 'http://elasticsearch:9200/',
            'INDEX_NAME': 'haystack',
        },
    }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "postgres",
            'USER': "postgres",
            'PASSWORD': "postgres",
            'HOST': "postgres",
            'PORT': 5432
        }
    }
