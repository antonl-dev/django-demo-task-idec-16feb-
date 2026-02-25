# Notes Management API

A robust CRUD REST API for managing personal notes, built with Django and Django REST Framework. This project was developed entirely in a Termux (Android) environment.

## 🚀 Features

- **Authentication**: User registration and login with Token-based authentication.
- **CRUD Operations**: Full Create, Read, Update, and Delete functionality for notes.
- **Data Privacy**: Strict object-level permissions. Users can only access, edit, or delete notes they own.
- **Archive System**: Notes can be archived. Archived notes are hidden from the main list by default but can be retrieved via query parameters.
- **Bonus - Search**: Filter notes by title or content using keywords.
- **Bonus - Pagination**: List endpoints are paginated (10 items per page) for performance.

## 🛠 Tech Stack

- **Language**: Python 3.12
- **Framework**: Django
- **API Library**: Django REST Framework (DRF)
- **Database**: SQLite3
- **Environment**: Termux (Android)

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd notes_api
   ```

2. **Install Dependencies**:
   ```bash
   pip install django djangorestframework
   ```

3. **Apply Migrations**:
   ```bash
   python manage.py makemigrations api
   python manage.py migrate
   ```

4. **Run the Server**:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## 📖 API Documentation

### Authentication
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/register/` | POST | Register a new user |
| `/api/login/` | POST | Login and receive an Auth Token |

### Notes (Requires Token)
All Note requests must include the header: `Authorization: Token <your_token>`

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/notes/` | GET | List all active (non-archived) notes |
| `/api/notes/` | POST | Create a new note |
| `/api/notes/{id}/` | GET | Retrieve a specific note |
| `/api/notes/{id}/` | PUT | Update a note (Replace) |
| `/api/notes/{id}/` | PATCH | Update a note (Partial) |
| `/api/notes/{id}/` | DELETE | Delete a note |

### Filtering & Search
- **Show Archived Notes**: `GET /api/notes/?archived=true`
- **Search Notes**: `GET /api/notes/?search=keyword`

## 🧪 Example Requests (using Curl)

### Login to get Token
```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password": "password123"}'
```

### Create a Note
```bash
curl -X POST http://127.0.0.1:8000/api/notes/ \
-H "Authorization: Token <your_token>" \
-H "Content-Type: application/json" \
-d '{"title": "Project Note", "content": "Complete the README"}'
```

### Search for a Note
```bash
curl -X GET "http://127.0.0.1:8000/api/notes/?search=Project" \
-H "Authorization: Token <your_token>"
```

## 📝 Design Decisions
- **ViewSet Logic**: Used `ModelViewSet` to handle CRUD logic efficiently while keeping the code clean and maintainable.
- **Custom Permissions**: Implemented an `IsOwner` permission class to enforce strict data ownership at the object level.
- **Query Overriding**: Overrode `get_queryset` to ensure users never accidentally see another user's data and to handle the toggle between active and archived notes.
