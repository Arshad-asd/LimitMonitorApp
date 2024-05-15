# Limit Monitor Application

This project is a limit monitor application built using Django, designed to fetch weather data, compare it with user-defined criteria, and trigger actions based on specified conditions. The application offers CRUD operations for managing monitoring criteria records and includes functionality to update record statuses based on predefined conditions.

## Features:
- **Monitoring Logic**: Implements logic to compare fetched weather data with user-defined criteria using various comparison operators.
- **CRUD Operations**: Allows users to Create, Read, Update, and Delete monitoring criteria records through a user-friendly interface.
- **Status Update**: Defines conditions for updating record statuses and implements a scheduler task to automate status updates based on predefined criteria.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Arshad-asd/LimitMonitorApp.git
```

2. Create and activate a virtual environment:

```bash
python -m venv env
```

```bash
# On Windows: .\env\Scripts\activate
# On macOS/Linux: source venv/bin/activate
```

```bash
cd backend
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the development server:

```bash
python manage.py runserver
```

6. Access the API at [http://localhost:8000/api/](http://localhost:8000/api/)

## API Endpoints


#### 1. User Management:

- `POST /api/users/register/`: Register a new user.
- `POST /api/users/login/`: Log in an existing user.
  
#### 1. Criteria Management:
- `POST /api/weather/user-criteria/`:
- `POST /api/weather/user-criteria/<int:pk>`:

## API Documentation


### `POST /api/user/register/`

**Description:**

Create a new User.

**Request:**
- **Method:** `POST`
- **Endpoint:** `/api/user/register/`
- **Body:**
  - `username` (string, required): User's username.
  - `email` (string, required): User's email.
  - `password` (string, required): User's password. "Password must be at least 6 characters long and contain at least one uppercase letter, one lowercase letter, and one digit."

**Response:**
- **Success Response:**
  - **Status Code:** 201 Created
  - **Body:**
    ```json
    {
      "id": 1,
      "email": "jhon@example.com"
      "username": "jhon"
    }
    ```

- **Error Response:**
  - **Status Code:** 400 Bad Request
  - **Body:**
    ```json
    {
      "error": "Invalid data. Please provide valid information."
    }
    ```

    ### `POST /api/login/`

**Request:**
- **Method:** `POST`
- **Endpoint:** `/api/login/`
- **Body:**
  - `email` (string, required): User's email.
  - `password` (string, required): User's password.

**Response:**
- **Success Response:**
  - **Status Code:** 200 OK
  - **Body:**
    ```json
    {
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...",
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9..."
    }
    ```

- **Error Response:**
  - **Status Code:** 401 Unauthorized
  - **Body:**
    ```json
    {
      "error": "Invalid credentials"
    }
    ```

