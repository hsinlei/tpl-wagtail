from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5+f#!xn=hj^u#=cr9@pz@@5cf7bqf0ymy=8uyfpx_zvxpght3='

ADMINS = (
    ('Charlene Wang', 'hsinlei.w@gmail.com'),
    ('Michael Yin', 'admin@michaelyin.info'),
    # ('Charlene Wang', 'hsinlei.w@gmail.com'),
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['54.234.209.28', 'localhost', '*']

try:
    from .local import *
except ImportError:
    pass
