#Description
The Election Voting System is a Django-based web application for small-scale elections, such as college student council, club leadership, or internal polls. Users can register, log in, vote for candidates, and view results in real-time. Admins can manage candidates easily through the Django Admin panel.
# Election Voting System

## Tech Stack
- Python 3.12
- Django 5.2.6
- Bootstrap 5
- SQLite (database)

## Features
- User Registration & Login
- Cast Vote
- View Results
- Admin can add candidates

## Run Project
1. Clone repo: `git clone <repo_url>`
2. Create virtual environment: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`
