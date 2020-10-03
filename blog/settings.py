"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# import cloudinary
# import cloudinary.uploader
# import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("BLOG_SECRET_KEY")

#only for development
# SECRET_KEY = "fjdlkfjsoijhjiru2389r3tnmnn8430"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('BLOG_DEBUG_VALUE')=="True")

#only for development
# DEBUG= True
# DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0','localhost','127.0.0.1']

#only for production
ALLOWED_HOSTS.append(os.environ.get('HOST_NAME'))


# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #creates apps
    'home',
    'blogs',
    'authors',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#whitenoise middleware for managing static files during production not for image files.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#database for production
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('BLOG_DATABASE_ENGINE'),
        'NAME': os.environ.get('BLOG_DATABASE_NAME'),
        'HOST': os.environ.get('BLOG_DATABASE_HOST'),
        'PORT': os.environ.get('BLOG_DATABASE_PORT'),
        'USER': os.environ.get('BLOG_DATABASE_USER'),
        'PASSWORD': os.environ.get('BLOG_DATABASE_PASSWORD'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

#static files from all apps will be collected here when collectstatic command is executed
#only used in production
# STATIC_ROOT=os.path.join(BASE_DIR,'static')


#not necessary during production

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static")
]

#used to create the STATIC_ROOT folder if it is not created during collectstatic command
# os.makedirs(STATIC_ROOT, exist_ok=True)

 
MEDIA_ROOT= os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'


#cloudinary configurations details for storing images and other media

# cloudinary.config( 
#   cloud_name = os.environ.get('BLOG_CLOUD_NAME'), 
#   api_key = os.environ.get('BLOG_API_KEY'), 
#   api_secret = os.environ.get('BLOG_API_SECRET') 
# )