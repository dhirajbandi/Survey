# Pollster Django Web App

## Overview
Pollster is a simple Django-based web application that allows users to create and vote on polls. This project was developed as part of research work, leveraging Django’s **MTV (Model-Template-View)** architecture.

## Features
- **Create Polls**: Users can add questions and multiple-choice answers.
- **Vote on Polls**: Users can vote on the available poll options.
- **View Poll Results**: The app displays poll results dynamically after voting.
- **Admin Panel**: A Django-admin panel is set up to manage polls.

## Project Structure

### 1. `models.py`
- Defines the database models for the application:
  - `Question` model stores poll questions along with their publication date.
  - `Choice` model stores poll choices and keeps track of vote counts.

### 2. `views.py`
- Handles requests and responses:
  - `index(request)`: Displays the latest poll questions.
  - `detail(request, question_id)`: Shows specific question details and available choices.
  - `results(request, question_id)`: Displays poll results.
  - `vote(request, question_id)`: Registers a vote and updates the count.

### 3. `urls.py`
- Defines URL patterns for the application:
  - `/` → Displays the poll index page.
  - `/<question_id>/` → Shows question details.
  - `/<question_id>/results` → Displays results of a poll.
  - `/<question_id>/vote` → Handles voting action.

### 4. `admin.py`
- Customizes Django Admin:
  - Registers `Question` and `Choice` models.
  - Enhances admin with inlined choices for easy management.

### 5. `apps.py`
- Configures the `polls` application.

### 6. `tests.py`
- Placeholder for test cases.

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd pollster
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   ```

3. Install dependencies:
   ```bash
   pip install django
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

7. Access the app in your browser:
   - **Frontend**: http://127.0.0.1:8000/polls/
   - **Admin Panel**: http://127.0.0.1:8000/admin/

## Author
**Dhiraj Bandi**  
Email: dhirajbandi2000@gmail.com  
GitHub: [your-github-profile]

---
This project was developed as part of research and is open for improvements.
