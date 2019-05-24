DEBUG = False
ALLOWED_HOSTS = ['*']




DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'url_n',
        'USER':'nikolay',
        'PASSWORD':'12345678',
        'HOST':'localhost',
        'PORT':''

    }
}