# LMSY Gallery Vault — Photo Album System

A secure, warm-minimalist photo sanctuary engineered with Django, PostgreSQL, and Cloudinary for decentralized asset storage. This platform implements strict native backend Role-Based Access Control (RBAC) to isolate user environments and secure media streams.

---

# Features

- User Authentication (Login, Logout, Registration)
- Role-Based Access Control (RBAC)
  - Standard Users
  - Album Administrators
- CRUD Operations for Albums and Photos
- Cloudinary Image Upload & Storage
- Responsive User Interface
- PostgreSQL Database Integration
- Production Deployment on Render
- Secure Environment Variables Configuration

---

# Technologies Used

- Python
- Django
- PostgreSQL
- Cloudinary
- HTML5 / CSS3 / Bootstrap
- Render

---

# System Architecture

This project follows industry-standard Django architecture practices:

- Class-Based Views (CBVs) for all CRUD operations
- Django Authentication System for secure login and user management
- Role-Based Access Control using Django Groups and Permissions
- Cloudinary for cloud image storage
- PostgreSQL as the production database
- Environment Variables for sensitive credentials

---

# Project Structure

```bash
photo_album/
│
├── albums/
├── users/
├── templates/
├── static/
├── photo_album/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── requirements.txt
├── manage.py
├── .env
└── README.md
```

---

# Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/Shangg20/Photo-Album-Project.git
cd photo-album-management
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

---

# Run Development Server

```bash
python manage.py runserver
```

Visit:

```bash
http://127.0.0.1:8000/
```

---

# Cloudinary Configuration

Install Cloudinary packages:

```bash
pip install cloudinary django-cloudinary-storage
```

Add the following to `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'cloudinary',
    'cloudinary_storage',
]

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

---

# Role-Based Access Control (RBAC)

The application implements RBAC using Django Groups and Permissions.

## Standard User

Can:
- View albums
- Upload photos
- Edit own content

Cannot:
- Manage other users
- Delete system-wide content

---

## Album Administrator

Can:
- Manage all albums
- Delete any photo
- Manage users and permissions

---

# Class-Based Views Used

The system utilizes Django CBVs such as:

- ListView
- DetailView
- CreateView
- UpdateView
- DeleteView
- LoginView
- LogoutView

Example:

```python
from django.views.generic import ListView
from .models import Album

class AlbumListView(ListView):
    model = Album
    template_name = 'albums/album_list.html'
```

---

# Deployment on Render

## Deployment Steps

1. Push project to GitHub
2. Create PostgreSQL database on Render
3. Create a new Web Service on Render
4. Connect the GitHub repository
5. Add environment variables
6. Deploy application

---

# Build Command

```bash
./build.sh
```

---

# Start Command

```bash
gunicorn core.wsgi:application
```

---

# Production Security Notes

- DEBUG disabled in production
- Secret keys stored in environment variables
- Cloudinary used instead of local media storage
- PostgreSQL used for scalable production database management

---

# requirements.txt Example

```txt
Django
gunicorn
psycopg2-binary
cloudinary
django-cloudinary-storage
dj-database-url
python-decouple
whitenoise
Pillow
```

---

# Live Application URL

```txt
https://photo-album-project-44b6.onrender.com
```

---

# GitHub Repository

```txt
https://github.com/Shangg20/Photo-Album-Project.git
```

---

# Future Improvements

- Image tagging system
- Album sharing
- Search and filtering
- REST API integration
- Drag-and-drop uploads
- Activity logs

---

# License

This project is for educational purposes.
