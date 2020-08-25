# Crisis Management System for CZ3003 SASD
This project aims to develop a full-stack Django web application with the purpose of providing information to civilians regarding a crisis.
Civilians can report and publish crisis around Singapore as well as view all reported crisis through a map (using Google Maps API)
Civilians are also notified of Dengue status, and pollution levels through data provided from Government API.



# How to use
1. Install virtualenv (pip install virtualenv)
2. Create virtualenv (virtualenv venv) 
3. Enable venv
4. Install dependencies (pip install -r requirements.txt) inside django folder not venv folder
6. python manage.py migrate
7. Runserver with -> python manage.py runserver
