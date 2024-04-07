# REFFERAL SYSTEM
## Setup
#### ****Please install python==3.8**** 
### ***URL : https://www.python.org/downloads/***
#### The first thing to do is to clone the repository:

$ git clone https://github.com/ashishk44-techqware/referral_system.git

#### Create a virtual environment to install dependencies in and activate it:
$ virtualenv env   (For Windows)  / python -m venv env (for ubuntu)
$ env\Scripts\activate (For Windows) / source env/bin/activate  (for ubuntu)

#### Then install the dependencies:
(env)$ pip install -r requirements.txt

Once pip has finished downloading the dependencies:

#### Run these Command For migrate the project:-

(env)$ python manage.py makemigrations
(env)$ python manage.py migrate

(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver

```And navigate to http://127.0.0.1:8000/```

```If you want to register as a User http://127.0.0.1:8000/api/v1/register ```
