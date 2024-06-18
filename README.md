# Medical Appointment Scheduler

## Overview

The Medical Appointment Scheduler is a Flask-based web application designed to manage medical appointments efficiently. It allows healthcare providers to schedule appointments, send reminders, and maintain patient records.

## Features

- User authentication (registration and login)
- Schedule and manage appointments
- Add and view patient information
- User-friendly interface

## Project Structure

medical_scheduler/
├── app.py
├── models.py
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── appointment.html
│   └── patient.html
└── README.md


## Requirements
Python 3.x
Flask
Flask-SQLAlchemy

## Setup
Clone the repository:
git clone https://github.com/NagaBharadwaj/medical_scheduler.git
cd medical_scheduler

Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the dependencies:
pip install Flask Flask-SQLAlchemy

Run the application:
python app.py
Open a web browser and navigate to http://127.0.0.1:5000.

## Usage
Register a new user:
Navigate to the registration page: http://127.0.0.1:5000/register
Fill out the form to create a new user account.
Login:
Navigate to the login page: http://127.0.0.1:5000/login
Enter your credentials to access the dashboard.
Dashboard:

View scheduled appointments.
Access links to schedule new appointments and add new patients.
Schedule Appointment:

Navigate to http://127.0.0.1:5000/appointment
Fill out the form to schedule a new appointment.
Add Patient:

Navigate to http://127.0.0.1:5000/patient
Fill out the form to add a new patient.
