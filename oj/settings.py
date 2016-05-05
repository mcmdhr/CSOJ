# coding=utf-8
"""
Django settings for oj project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from __future__ import absolute_import
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# 判断运行环境
ENV = os.environ.get("oj_env", "local")

if ENV == "local":
    from .local_settings import *
elif ENV == "server":
    from .server_settings import *

from .custom_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'account',
    'announcement',
    'utils',
    'group',
    'problem',
    'admin',
    'submission',
    'contest',
    'judge',
    'judge_dispatcher',

    'rest_framework',
)

if DEBUG:
    INSTALLED_APPS += (
        # 'debug_toolbar',
        'rest_framework_swagger',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'admin.middleware.AdminRequiredMiddleware',
    'account.middleware.SessionSecurityMiddleware'
)

ROOT_URLCONF = 'oj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': OJ_TEMPLATE_DIRS,
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

WSGI_APPLICATION = 'oj.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'account.User'

LOG_PATH = "log/"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
        # 日志格式
    },
    'handlers': {
        'django_error': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH + 'django.log',
            'formatter': 'standard'
        },
        'app_info': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH + 'app_info.log',
            'formatter': 'standard'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        'app_info': {
            'handlers': ['app_info', "console"],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['django_error', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        }
    },
}

if DEBUG:
    REST_FRAMEWORK = {
        'TEST_REQUEST_DEFAULT_FORMAT': 'json'
    }
else:
    REST_FRAMEWORK = {
        'TEST_REQUEST_DEFAULT_FORMAT': 'json',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        )
    }

# for celery
BROKER_URL = 'redis://%s:%s/%s' % (REDIS_QUEUE["host"], str(REDIS_QUEUE["port"]), str(REDIS_QUEUE["db"]))
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"

DATABASE_ROUTERS = ['oj.db_router.DBRouter']

TEST_CASE_DIR = os.path.join(BASE_DIR, 'test_case/')

IMAGE_UPLOAD_DIR = os.path.join(BASE_DIR, 'upload/')

# 用于限制用户恶意提交大量代码
TOKEN_BUCKET_DEFAULT_CAPACITY = 50

# 单位:每分钟
TOKEN_BUCKET_FILL_RATE = 2

# 是否显示所有人的提交, False就只显示自己的
SHOW_ALL_SUBMISSIONS_LIST = False
