# Student Management System

A simple Django-based Student Management System to manage students, subjects, and grades with an easy-to-use web interface.

## Features

- Add, view, edit, and delete students
- Manage subjects (add, update, delete)
- Assign and track student grades (activities, quizzes, exams)
- Responsive UI built with Bootstrap 5
- Clean, user-friendly dashboard for quick access

## Technologies Used

- Python 3.8+
- Django 4.2+
- Bootstrap 5
- SQLite (default Django DB, can be changed)

## Getting Started

Setup Instructions
- Clone the repository
- FINAL_PROJECT 
- activate a virtual environment (recommended)
# On Windows
- venv\Scripts\activate
# On macOS/Linux
- source venv/bin/activate
- Install dependencies 
- install pip install Django 
- pip install django djangorestframework
- cd Project
- run python manage.py runserver

### Prerequisites

- Python 3.8 or higher installed
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git <your-repo-url>

### API Endpoints
  
The application provides the following RESTful API endpoints:
   URLs
Resource	http://127.0.0.1:8000/api/
Students	http://127.0.0.1:8000/api/students/
Subjects	http://127.0.0.1:8000/api/subjects/
Grades	    http://127.0.0.1:8000/api/grades/
