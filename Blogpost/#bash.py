#bash

django-admin startproject post_project
cd post_project


python manage.py startapp posts
cd posts

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver