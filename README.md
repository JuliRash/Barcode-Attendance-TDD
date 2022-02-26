# Barcode Attendance System TDD 👨🏻‍🔧
This is a simple web application built with  **django** the code implements marking attendance and submitting it to the database via a barcode scanner.

It runs under officially Django supported versions:
* Django 3.1.
* Python 3 (3.2, 3.4, 3.5, 3.6)

![love](barcode.png)

## How to install locally

This Application can be installed by following the instructions below.

you must have **[python 3](https://www.python.org/downloads/)** > and  [pipenv](https://pypi.org/project/pipenv/)  installed

### Clone the repository

    $ git clone git@github.com:JuliRash/Barcode-Attendance-TDD.git

### Change the directory to the application folder.

    $ cd Barcode-Attendance-TDD

### Activate the virtualenv using pipenv

    $ pipenv shell

### Install the requirements for the project

    $ pip install -r requirements.txt

### Create the .env file from .env.example 

    $ cp .env.example .env

### Setup app lication

    $ python manage.py app_setup

### Edit the .env file created and set values to the variables.
webdriver for [chrome](https://chromedriver.chromium.org/downloads)
```bash
        SECRET_KEY=''
        DEBUG=True
        webdriver_path = ''
```
    


### Migrate the database: 
```bash
$ python manage.py migrate
```

### Start the App.
```bash
$ python manage.py runserver
```

### Run tests
```bash
$ python manage.py test
```

You can visit the application in this link below if the installation is successful.
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Create a super user to configure the application by filling the setup form in the django admin.
[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


