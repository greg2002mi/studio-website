# Studio website

Website written in Django API. contents can be edited or renewed either via dashboard or admin panel.

## Structure

- 12 sections 
	- adjustable header
- 3 forms
	- review form
	- Order requisition form
	- call me form
- integrated with telegram 
	- with a API key and telegram id it can be tuned to recieve messages upon order requisition and call me request.
     In settings.py:
```
   TELEGRAM_BOT_TOKEN = "here paste telegram bot api key"
   CHAT_ID = "telegram id of person who will recieve requests from visitors"
```

Text can be altered in message variable:
       orders.views.py
```
def order(request...
...
message = 

def call_me(request...
...
message = 
```
- Dashboard
	- 18 forms of content upload
		- CRUD features

## Database

POSTGRESQL has been used. But tt can be used with SQLLITE too, though recommended only during development stage.
In case of POSTGRESQL first create database.
in settings.py make sure to bind database with installed database. 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "database name",
        'USER': "postgres",
        'PASSWORD': "password",
        'HOST': "localhost",
        'PORT': "",
    }
}
```
In case of SQLLITE no changes needed. Django settings are set to sqllite by default.

## Template

A free Template has been used, which has been taken from Colorlib.com  

## Installation

1. create virtual environment ```python -m venv venv```
2. install all dependancies using req file. ```pip install -r /path/to/req```
3. create project ``` django-admin startproject name_of_the_project ```. (in my case its kamiweb)
    if you have named a project as kamiweb, then just copy everything from this repository into you project.
   otherwise copy all except kamiweb from this repo to your project folder. then replace all of the files in your app folder (where settings.py is located) with files located in kamiweb folder (settings.py, urls.py).
5. create database based on models of this project
  ``` python manage.py makemigrations ```
   followed by 
   ``` python manage.py migrate ```
6. create superuser ``` python manage.py createsuperuser ```
7. and start project ``` python manage.py runserver ```
8. go to dashboard by this link ``` 127.0.0.1:8000/dashboard ```

So here we go. populate all of the sections via dashboard, and website is ready to use.

## Please note

As I am not a web designer, the template has been poorly adopted to this website. therefore I recommend to use other template of your choice.

So here it is. 

Bye!
