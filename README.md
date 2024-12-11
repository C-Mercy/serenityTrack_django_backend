#serenityTrack_django_backend
# SerenityTrack Django Backend

This project is the backend server for the SerenityTrack application, built using Django and PostgreSQL. It provides the REST API endpoints required for the frontend application to function and database connection to a postgres Database.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Environment Variables](#environment-variables)
- [Database Migrations](#database-migrations)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/serenityTrack_django_backend.git
    cd serenityTrack_django_backend
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add the following variables:
    ```plaintext
    DATABASE_ENGINE=django.db.backends.postgresql
    DATABASE_NAME=your_database_name
    DATABASE_USER=postgres
    DATABASE_PASSWORD=your_password_here
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    SECRET_KEY=your_secret_key_here
    ```

## Usage

To start the development server, use the following commands:

1. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Create a superuser for accessing the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

3. Start the development server:
    ```bash
    python manage.py runserver
    ```

The server will be running at `http://localhost:8000`.

## Features

- **User Management**: Registration, login, and user profile management.
- **Journal Entries**: Create, read, update, and delete journal entries.
- **Episodes Tracking**: Manage and track episodes including triggers, behaviors, and interventions.
- **Admin Panel**: Django admin panel for managing all data.

## Environment Variables

Ensure that the `.env` file in the root directory contains the necessary environment variables:
```plaintext
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=your_database_name
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password_here
DATABASE_HOST=localhost
DATABASE_PORT=5432
SECRET_KEY=your_secret_key_here
