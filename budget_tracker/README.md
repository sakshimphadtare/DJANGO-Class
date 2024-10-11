# Personal Budget Tracker
 
## git repository link : https://github.com/sakshimphadtare/budget_tracker.git

A simple budget tracking application built with Django and Django REST Framework. This application allows users to manage their transactions and budgets efficiently.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create, read, update, and delete transactions.
- Create and manage budgets.
- RESTful API for transaction and budget management.

## Technologies Used

- Python 3.x
- Django
- Django REST Framework
- SQLite (default database)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sakshimphadtare/Budget_Tracker.git
   cd Budget_Tracker

2. **Create and activate a virtual environment:**
python -m venv env
source env/bin/activate  

3. **Install the required packages:**
pip install <required package>

4. **Run migrations:**
py manage.py makemigrations
py manage.py migrate

5. **runserver**
py manage.py runserver

you can now access the application at http://127.0.0.1:8000/api/transactions.

**Usage**
Access the API: You can use tools like Postman to interact with the API.
Available Endpoints:
Transactions
GET /api/transactions/ - List all transactions
POST /api/transactions/new/ - Create a new transaction
GET /api/transactions/<pk>/ - Retrieve a specific transaction
DELETE /api/transactions/<pk>/ - Delete a specific transaction

**Budgets**
GET /api/budgets/ - List all budgets
POST /api/budgets/ - Create a new budget
GET /api/budgets/<pk>/ - Retrieve a specific budget
DELETE /api/budgets/<pk>/ - Delete a specific budget