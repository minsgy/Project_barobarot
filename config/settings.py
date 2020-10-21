"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#'ff+)kt1i=zjv-u20+1&5j#il*@^xl88@10mi7$q#1e3w(y!%-s'
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))

ALLOWED_HOSTS = ['*']

THIRD_PARTY_APPS = [
    'django.contrib.humanize', # 금액 표시 ',' 표시용
    'mathfilters',# 템플릿 필터 수학 연산용
    'storages',
]  # 패키지 기능 app

PROJECT_APPS = [  # ADMIN이 만든 APP
    'users.apps.UsersConfig',
    'engineers.apps.EngineersConfig',
    'core.apps.CoreConfig',
    'payments.apps.PaymentsConfig',
    'products.apps.ProductsConfig',
    'comments.apps.CommentsConfig',
]

DJANGO_APPS = [ # 장고 기본 app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 설치 app
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'DIRS': [os.path.join(BASE_DIR, "templates")], # 폴더 바깥으로 templates 통합
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


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr' # time field

TIME_ZONE = 'Asia/Seoul' # Asia 시간 대로 변경.

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # 개발자 관리 파일들을 static에 저장.
# media 파일 url 설정
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads') 
# 폴더 uploads가 생성 되면서 미디어 파일저장.
# imageField 저장 시 (upload_to="저장 할 폴더 지정")


# 원래의 User 모델의 값을 Custom 해주기 위해, USER MODEL을 CUSTOM 한 User 모델 지정
AUTH_USER_MODEL = "users.User"

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Django 기본 저장 시스템을 지정
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
# static 파일들을 s3 버킷에 저장하는 설정
# STATICFILES_STORAGE = 'config.storages.StaticStorage'
# media, static 폴더를 만들어 저장함.
MEDIAFILES_LOCATION = 'media'
# STATICFILES_LOCATION = 'static'
#
AWS_ACCESS_KEY_ID = 'AKIAVAXCAYWKPLFVBM3B'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'barobarot'