# EduFlow School Portal

## Project Overview

EduFlow School Portal is a Flask-based web application that allows students to register, log in, reset their passwords, and access a dashboard. The project demonstrates the use of Flask, SQLite, Docker, Docker Compose, GitHub, and GitHub Actions for Continuous Integration.

## Features

- Student Registration
- Student Login
- Forgot Password
- Student Dashboard
- SQLite Database
- Responsive User Interface

## Technologies Used

- Python 3.14
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Git
- GitHub
- Docker
- Docker Compose
- GitHub Actions

## Project Structure

```
EduFlow School Portal
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── static/
├── templates/
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/digitalella-creator/eduflow-school-portal.git
```

Navigate into the project:

```bash
cd eduflow-school-portal
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Or run using Docker Compose:

```bash
docker compose up
```

## CI/CD

This project uses GitHub Actions to automatically:

- Install Python
- Install project dependencies
- Verify Flask installation whenever code is pushed to the repository.

## Author

**Emmanuela**