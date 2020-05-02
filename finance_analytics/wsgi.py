"""
WSGI config for finance_analytics project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_analytics.settings')

application = get_wsgi_application()

# ========以下をすべて追加(11-3 デプロイの実施)========
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
