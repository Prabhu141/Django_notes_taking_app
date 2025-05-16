# Django Note-Taking App – Session-Based Authentication

## Developer: Prabhu

## Features:
- Custom user model using email
- Session-based login and logout
- Note creation and viewing per user
- SQLite3 database used

## How to Run:
1. Install dependencies: `pip install -r requirements.txt`

2. Run migrations:
    python manage.py makemigrations
    python manage.py migrate

3. Create a superuser: `python manage.py createsuperuser`


4. Run server: `python manage.py runserver`


#URLS

Register: http://127.0.0.1:8000/register/

Login: http://127.0.0.1:8000/login/


Home Page (after login): http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin

