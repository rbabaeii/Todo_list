"""
WSGI config for reza project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
# from whitenoise import WhiteNoise

# from reza import wsgi

# application = wsgi()
# application = WhiteNoise(application, root="/path/to/static/files")
# application.add_files("/path/to/more/static/files", prefix="more-files/")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reza.settings')

application = get_wsgi_application()
