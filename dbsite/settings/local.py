from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('DATABASE_ENGINE'),
#         'NAME': os.environ.get('DATABASE_NAME'),
#         'USER': os.environ.get('DATABASE_USER'),
#         'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
#         'HOST': os.environ.get('DATABASE_HOST'),
#         'PORT': '',
#     }
# }

# DATABASES = {
#    'default': {
#        'ENGINE': os.environ.get('DATABASE_ENGINE'),
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
