DEBUG = True

ALLOWED_HOSTS = ('*',)

BOT_TOKEN = ''
BOT_NAME = ''

PAYME_LOGIN = 'Paycom'
PAYME_PASSWORD = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'auth_model',
        'USER': 'postgres',
        'PASSWORD': '20010508',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = ''  # SendGrid API Key
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = ''