# ArgoProject
This is the repo for SDD project
## Introduction
ArgoProject is a customizable application service provider designed to allow users to create applications through a Django-based website. Form creators can create and manage applications using it and distribute them via email from the website. Submissions from applicants can also be viewed and filter based on given criteria.

First time users register for the website through the sign-up page, and then may log in to the system. The application creator can be accessed by clicking the 'Start' button in the Application Creator section. From there, users can create and manage forms for the programs they wish to use them for. 

## Installing
Make sure you have already installed Python 3.7, then install the Django 2.1.5 by entering:
```
pip install Django==2.1.5
```
If you are using macOS Catalina or higher, which has the Python pre-installed, use the following command instead:
```
pip3 install Django==2.1.5
```
## Running
Open the Project directory, entering:
```
python manage.py migrate
python manage.py runserver
```
Again if you are using macOS Catalina or higher, use the following command instead:
```
python3 manage.py migrate
python3 manage.py runserver
```
To create a adminstartor of the website, use the command:
```
python manage.py createsuperuser
```
