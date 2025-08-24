from .base import *
from .secret import SECRET_LOCAL

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": SECRET_LOCAL.get("DB_NAME"),
        "USER": SECRET_LOCAL.get("DB_USER"),
        "PASSWORD": SECRET_LOCAL.get("DB_PASS"), 
        "HOST": SECRET_LOCAL.get("DB_HOST"),
        "PORT": SECRET_LOCAL.get("DB_PORT"),
        "OPTIONS": {
            "sql_mode": "STRICT_TRANS_TABLES",
        },
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static/"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media_local/"