from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS= True
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD =  env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL= "info@drippers-island.com"
DOMAIN =  env("DOMAIN")
SITE_NAME = "Drippers Island"


DATABASES = {
    "default": {
        "ENGINE": env("DATABASE_ENGINE"),
        "NAME": env("DATABASE_DB"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
    }
}