# user-management-rest-API
This is a simple user management API using the django rest framework

#simple rest API
#internpulse cohort 3
 
 Python 3.x
- Django 3.x or 4.x
- Django Rest Framework

### Installation

1. **Install Django and Django Rest Framework**:

    ```bash
    pip install django djangorestframework
    ```

2. **Create a new Django project and app**:

    ```bash
    django-admin startproject user_management
    cd user_management
    django-admin startapp users
    ```

3. **Configure settings**:

    Add `rest_framework` and `users` to your `INSTALLED_APPS` in `user_management/settings.py`:

    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'users',
    ]
    ```

4. **Database setup**:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

5. **Create and apply migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    ### Create a New User

- **URL**: `/users/create/`
- **Method**: `POST`
- **Description**: Create a new user.
- **Request Body**:
    ```json
    {
        "username": "newuser",
        "first_name": "New",
        "last_name": "User",
        "email": "newuser@example.com",
        "password": "newpassword"
    }
    ```
- **Response**:
    - **Status**: `201 Created`
    - **Body**:
        ```json
        {
            "id": 1,
            "username": "newuser",
            "first_name": "New",
            "last_name": "User",
            "email": "newuser@example.com"
        }
        ```

### Retrieve User Information

- **URL**: `/users/retrieve/`
- **Method**: `GET`
- **Description**: Retrieve user information by ID or username.
- **Query Parameters**:
    - `id`: User ID (integer)
    - `username`: Username (string)
- **Response**:
    - **Status**: `200 OK`
    - **Body** (example for retrieval by ID):
        ```json
        {
            "id": 1,
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com"
        }
        ```
    - **Status**: `404 Not Found` (if user does not exist)
    - **Status**: `400 Bad Request` (if neither `id` nor `username` is provided)

### Update User Information

- **URL (by ID)**: `/users/update/<int:pk>/`
- **URL (by username)**: `/users/update/`
- **Method**: `PUT`
- **Description**: Update user information by ID or username.
- **Request Body**:
    ```json
    {
        "username": "updateduser"
    }
    ```
- **Query Parameters** (for update by username):
    - `username`: Old username (string)
- **Response**:
    - **Status**: `200 OK`
    - **Body**:
        ```json
        {
            "id": 1,
            "username": "updateduser",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com"
        }
        ```
    - **Status**: `404 Not Found` (if user does not exist)
    - **Status**: `400 Bad Request` (if neither `id` nor `username` is provided)

### Delete a User

- **URL (by ID)**: `/users/delete/<int:pk>/`
- **URL (by username)**: `/users/delete/`
- **Method**: `DELETE`
- **Description**: Delete a user by ID or username.
- **Query Parameters** (for delete by username):
    - `username`: Username (string)
- **Response**:
    - **Status**: `204 No Content`
    - **Status**: `404 Not Found` (if user does not exist)
    - **Status**: `400 Bad Request` (if neither `id` nor `username` is provided)

### List All Users (User Directory)

- **URL**: `/users/directory/`
- **Method**: `GET`
- **Description**: List all users.
- **Response**:
    - **Status**: `200 OK`
    - **Body**:
        ```json
        [
            {
                "id": 1,
                "username": "testuser",
                "first_name": "Test",
                "last_name": "User",
                "email": "testuser@example.com"
            },
            {
                "id": 2,
                "username": "anotheruser",
                "first_name": "Another",
                "last_name": "User",
                "email": "anotheruser@example.com"
            }
        ]
        ```

## Example Requests

### Create a New User

```bash
curl -X POST http://127.0.0.1:8000/users/create/ \
    -H "Content-Type: application/json" \
    -d '{
        "username": "newuser",
        "first_name": "New",
        "last_name": "User",
        "email": "newuser@example.com",
        "password": "newpassword"
    }'


## Retrieve User Information by ID
curl -X GET "http://127.0.0.1:8000/users/retrieve/?id=1"
