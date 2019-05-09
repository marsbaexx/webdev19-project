"""
<<<<<<< HEAD
WSGI config for todo_back project.
=======
WSGI config for mysite project.
>>>>>>> 9eada6e416fa4b1441eaf9455c6ea41dac34afa4

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_back.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
>>>>>>> 9eada6e416fa4b1441eaf9455c6ea41dac34afa4

application = get_wsgi_application()
