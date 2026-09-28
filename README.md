# CRM Management System

A complete Customer Relationship Management (CRM) web application built with Python, Django, SQLite and Bootstrap-style responsive CSS.

## Features
- Dashboard with customer statistics
- Customer CRUD: Add, View, Edit, Delete
- Search and status filtering
- Customer profile/details page
- Reports page with business/customer statistics
- About and Contact pages
- Django Admin support
- Responsive light-themed interface
- Clean navigation with no duplicate links
- SQLite database
- Demo customer data can be added from the Django shell

## Run in VS Code / Command Prompt

1. Open this folder in VS Code.
2. Open Terminal.
3. Create a virtual environment:
   `python -m venv venv`
4. Activate it on Windows:
   `venv\Scripts\activate`
5. Install dependencies:
   `pip install -r requirements.txt`
6. Create the database:
   `python manage.py migrate`
7. Create an admin account:
   `python manage.py createsuperuser`
8. Start the server:
   `python manage.py runserver`
9. Open:
   `http://127.0.0.1:8000/`

Admin:
`http://127.0.0.1:8000/admin/`

## Main navigation
- Dashboard
- Customers
- Add Customer
- Reports
- About
- Contact

Each navigation item opens its own page.

## Technology
Python | Django | SQLite | HTML | CSS | JavaScript

## Project structure
crm_project/
crm/
templates/
static/
manage.py
requirements.txt
README.md
