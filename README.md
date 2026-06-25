# Product Dashboard API

This is a Django REST Framework application for a product dashboard with user authentication and product management features.

## Features

- User registration and authentication (JWT-based)
- Role-based access control (Admin/User roles)
- Product CRUD operations (Admin only)
- Product search and ordering functionality
- Image upload support for products and user profiles

## Technology Stack

- Python 3.x
- Django 6.0.6
- Django REST Framework
- Django REST Framework Simple JWT
- SQLite (default database)

## Project Structure

```
product-dashboard/
├── accounts/          # User authentication app
├── products/          # Product management app
├── config/            # Project configuration
├── media/             # Uploaded media files
├── manage.py          # Django management script
└── db.sqlite3         # SQLite database file
```

## Installation

1. Clone or navigate to the project directory:
   ```
   cd product-dashboard-cybexel
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install django djangorestframework djangorestframework-simplejwt
   ```

4. Apply database migrations:
   ```
   cd product-dashboard
   python manage.py migrate
   ```

5. (Optional) Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication

| Endpoint                | Method | Description                  |
|-------------------------|--------|------------------------------|
| `/api/auth/register/`   | POST   | Register a new user          |
| `/api/auth/login/`      | POST   | User login and get tokens    |
| `/api/auth/token/refresh/` | POST | Refresh JWT token            |

### Products (Admin only)

| Endpoint                  | Method | Description                  |
|---------------------------|--------|------------------------------|
| `/api/products/`          | GET    | List all products            |
| `/api/products/`          | POST   | Create a new product         |
| `/api/products/{id}/`     | GET    | Retrieve a specific product  |
| `/api/products/{id}/`     | PUT    | Update a specific product    |
| `/api/products/{id}/`     | PATCH  | Partially update a product   |
| `/api/products/{id}/`     | DELETE | Delete a specific product    |

## User Roles

- **Admin**: Has full access to product CRUD operations
- **User**: Can authenticate but cannot modify products

## License

See LICENSE file for details.
