#=============================================================================
# Author       : MaxMao
# Email        : 623742750@qq.com
# Last modified: 2016-05-04 13:54
# Filename     : wsgi.py
# Description :
#=============================================================================
"""
WSGI config for csoj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oj.settings")

application = get_wsgi_application()
