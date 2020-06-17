import environ
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# 環境変数
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
        # 'PORT': '',
    }
}
# 外部ファイルから呼ぶ
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': '',
#         'USER': DATABASE_USER,
#         'PASSWORD': DATABASE_PASSWORD,
#         'HOST': 'localhost',
#         # 'PORT': os.envrion.get('DATABASE_PORT'),
#         'PORT': '',
#     }
# }
