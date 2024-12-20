"""
Django settings for LMS_SYSTEM project.

Generated by 'django-admin startproject' using Django 5.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOGIN_URL = 'login'  # Default URL to redirect if not logged in
# settings.py
LOGIN_REDIRECT_URL = ''

# Add or update media settings for handling uploaded files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# STATIC_URL = '/staticfiles/'
# STATIC_URL for development
STATIC_URL = '/static/'

# STATICFILES_DIRS is correct - it tells Django where to look for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Custom static files directory
]


# settings.py
AUTH_USER_MODEL = 'user.User'  # Change 'user' to the name of your app

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

#Send email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'codinglmsfsa@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'adst vdek luiv zkny'  # Your email password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Set the default from email

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h+p6t3%50m)_a15%4&i*q_ule5a_$566#wu=f_5uvlapiqq%5v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['codinglmsfsa.pythonanywhere.com']

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# CKEditor configuration
CKEDITOR_UPLOAD_PATH = "uploads/"  # Path where uploaded images will be stored
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 'auto',
    },
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'debug_toolbar',
    'import_export',
    'ckeditor',
    'ckeditor_uploader',  #Optional: if you want to allow image uploads
    'widget_tweaks',

    
    'module_group',
    'training_program',
    'subject', 'student_materials', #for FSA subject

    'main', #for hompage

    'exercises', #Binh_Thang
    #ngattt
    'assessments', 'reports', 'group_enrollment', 'mylearning', 'certification', 
    'learning_path',

    #group01
    'user', 'role', 'department', 

    #group02
    'course', 'feedback', 'forum', 

    #group03
    'quiz', 'std_quiz', 'course_Truong', 'tools', # 'std_course',

    #group04
    'chat', 'chatapp', 'thread', 'collaboration_group', 

    #group05 
    'activity', 'ai_insights', 'analytics_report', 'assignment', 'certificate', #'course_completion',  
    'performance_analytics', 'progress_notification', 'student_performance', 
    'user_progress', 'user_summary', 'book'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Add this line
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'activity.activity_tracking_middleware.ActivityTrackingMiddleware'

]

ROOT_URLCONF = 'LMS_SYSTEM.urls'

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


WSGI_APPLICATION = 'LMS_SYSTEM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'LMS',
#         'USER': 'postgres',
#         'PASSWORD': '1234567890',
#         'HOST': 'localhost',  # Set to the appropriate host if using a remote server
#         'PORT': '5432',       # Default PostgreSQL port
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'