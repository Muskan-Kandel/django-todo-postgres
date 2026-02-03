Overview
This is a fully functional CRUD (Create, Read, Update, Delete) application developed using Django ORM with a PostgreSQL database. The application allows users to register, log in, and manage their own private list of tasks securely.

Features
1) User Authentication – Secure user registration and login system
2) User Isolation – Each user can access only their own tasks
3) Modern UI – Clean and responsive interface using Bootstrap
4) Full CRUD Functionality – Create, read, update, and delete tasks

Tech Stack
1) Backend: Django 6.0
2) Database: PostgreSQL
3) Frontend: HTML5, CSS3, Bootstrap 5
4) Form Management: Django Crispy Forms

Installation and Setup
1) Database Configuration
Ensure PostgreSQL is installed and running. Create a database named "todo".

2) Environment Setup
Clone the repository and create a virtual environment:

python -m venv venv

Activate the virtual environment:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3) Install Dependencies
pip install -r requirements.txt

4) Apply Migrations
python manage.py migrate

5) Run the Server
python manage.py runserver

     
