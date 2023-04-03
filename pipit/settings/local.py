"""
Write local settings here, or override base settings
"""
from pipit.settings.base import *  # NOQA

DJANGO_SETTINGS_MODULE="pipit.settings.local"
ALLOWED_HOSTS=["127.0.0.1", "localhost", "leacards.com", "stage-leacards.com"]
SECRET_KEY="django-insecure-l-^tupr!-ye9*n4sylkb)h+c#8bb8wa69-)dsx=pb!93w-j=w2"
#MEDIA_PATH=/src/media
#STATIC_PATH=/src/static
DATABASE_NAME="leacardsdb"
DATABASE_USER="leauser"
DATABASE_PASSWORD="lea321"
DATABASE_HOST="localhost"
#APP_LOG_DIR=/mnt/persist/www/leacards/logs
#SENTRY_DSN=
#AWS_ACCESS_KEY_ID=
#AWS_SECRET_ACCESS_KEY=
#AWS_BUCKET_NAME=

VS_CODE_REMOTE_DEBUG = False
DEBUG = True
#TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # type: ignore[index]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Email notification url
WAGTAILADMIN_BASE_URL = "https://leacards.com.test:8081"

# Allow weak local passwords
AUTH_PASSWORD_VALIDATORS = []

#INTERNAL_IPS = get_env("INTERNAL_IPS", default="").split(",")

# Add django debug toolbar when using local version
"""
if get_env_bool("DEBUG_TOOLBAR", default=False):
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    INSTALLED_APPS += ["debug_toolbar"]

    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": "pipit.settings.local.show_toolbar"
    }
"""

# Allow django-debug-bar under docker
def show_toolbar(request):
    return True
