from pathlib import Path
from datetime import timedelta
from celery.schedules import crontab


BASE_DIR = Path(__file__).resolve().parent.parent.parent


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "dj_rest_auth",   
    "corsheaders",
    "drf_spectacular",
    "django_filters",
    "core",
    "accounts",
    "library",
    "borrowing",
    "reservation",
    "fines"
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SITE_ID = 1

REST_USE_JWT = True

REST_AUTH_TOKEN_MODEL = None

JWT_AUTH_COOKIE = "library-auth"

JWT_AUTH_REFRESH_COOKIE = "library-refresh-token"

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Library Management System",
    "DESCRIPTION": "This is API documentation for library management system.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
}

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "core.User"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_BEAT_SCHEDULE = {
    "create_fines": {
        "task": "fines.tasks.create_fines",
        "schedule": crontab(hour=0, minute=10)
    }
}