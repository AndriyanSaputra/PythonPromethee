import os, django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


SECRET_KEY = 'e8*2@^#8g#$y!-rno(09*p3f^(=vh5e*00!nh^fva!*nkm=e)a'
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '10.10.1.139',
]

PROJECT_APPS = [
    'orm',
    'management.pekerja',
    'management.disiplin',
    'management.kesehatan',
    'management.petadua',
    'management.pko',
    'management.psikotes',
]

REQUIRED_APPS = [
    'material',
    'material.frontend',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = REQUIRED_APPS + PROJECT_APPS

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'


from app.config.auth import *
from app.config.database import *
from app.config.international import *
from app.config.static import *
from app.config.media import *
django.setup()
from app.config.template import *



