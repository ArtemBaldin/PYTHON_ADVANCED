python manage.py runserver
python manage.py migrate
python manage.py makemigrations

pip install django
cd /home/meta/Dropbox/Py/STUDY/PYTHON_ADVANCED/HW_4/project_Django
django-admin startproject plex
$ cd plex
python manage.py runserver
python manage.py migrate

python manage.py createsuperuser
python manage.py startapp core


# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
$ pip install django-debug-toolbar
settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'core',
    'debug_toolbar',
]




---
pip install flake8-import-order
flake8-builtins
flake8-print
