# Learning Log

Learning Log is an online journal system that lets you keep track of information you've learned about a particular topic. It can also be used for professional productivity tracking and much more. (Inspired by Eric Matthew's _Python Crash Course_ project

  <p align="center"> 
    <strong>Explore the documentation</strong>
    <br />
    <br />
    <a href="https://learning-log-app.fly.dev/">Live Production Website</a>
    ·
    <a href="https://github.com/Filbog/learning-log/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Filbog/learning-log/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Technical Details](#technical-details)
- [Running the Code on Your Local Machine](#running-the-code-on-your-local-machine)
- [Roadmap](#roadmap)
- [Contact](#contact)

## Project Description

Learning Log helps users create their own learning logs and keep a list of topics they're learning about. Whenever users learn something new about a topic, they can make an entry summarizing what they've learned. 
This project is built on top of the one covered in Eric Matthew's book, _Python Crash Course_ - of course with different coding solutions, additional functionality, custom styling and depolyment process completely from scratch.

## Features

- Sign up to start creating topics you're interested learning more about
- Create and manage learning logs
- Make entries summarizing new information learned
- Track your productivity and consistency
- View other user's public topics or display yours to the world

## Technical Details
### Back End and Database
- This App is built predominantly with Django framework
- For practice, I've used both generic class-based views and function views
- Django ORM used for communication with the database (PostgreSQL for production, SQLite for local environment)
- Classic CRUD implementation with creating, managing and deleting topics and entries associated with them
- Registration and user management: Django's built-in authentication system with custom registration view and form, enriched with sending email confirmation link for creating the user account
### Front End
- Django's templates were everything I needed to create the core of my app - minimalistic and without unnecessary distractions
- For styling, I've used Bootstrap 5
- Django Crispy Forms was used to render forms in the app.
### Deployment
- The app is fully up-and-running on https://learning-log-app.fly.dev/ 
- FlyIO was the platform of choice for deploying my app, despite having a ready-made solution in _Python Crash Course_. FlyIO is pretty reliable and its basic tier is better than what Platform.sh has to offer
- What led me to using FlyIO is its relative simplicity to create and connect a PostgreSQL database and establish environment variables such as email credentials or the app's secret key
- WhiteNoise package to handle static files (for production)

## Running the Code on Your Local Machine
### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Git
- A virtual environment tool (optional but recommended)

### Clone the Repository

```sh
git clone https://github.com/Filbog/learning-log.git
cd your-repo
```
### Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Dependencies
```sh
pip install -r requirements.txt
```
### Create and Configure the .env File
Create a .env file in the project root and add the following environment variables:
```
SECRET_KEY=your-secret-key
DEBUG=True
```
You can generate your 'SECRET_KEY' using:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
### Apply Migrations and Collect Static Files
```sh
python manage.py migrate
python manage.py collectstatic
```
### Run the Development Server
```sh
python manage.py runserver
```
Open your browser and navigate to http://127.0.0.1:8000 to see the application in action.

## Roadmap
Features I'd love to implement in the future:
- commenting other users' public topics and entries
- adding files like images, videos to the topic entries
- hashtag system to filter specific areas in which the users are interested in

## Contact
Message me via email: f.boguslawski101@gmail.com
Or on Linkedin: https://www.linkedin.com/in/filip-boguslawski/


