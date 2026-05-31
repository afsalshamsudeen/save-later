# SaveLinks

A simple and efficient link management platform that allows users to save, organize, and access important links for later use.

## Features

* User authentication and authorization
* Save links with title and description
* Organize links into categories
* Search saved links
* Edit and delete saved links
* Secure API using JWT authentication
* PostgreSQL database integration
* RESTful API architecture
* FastAPI automatic documentation

## Tech Stack

### Backend

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* JWT Authentication

### Development Tools

* Python 3.12+
* Uvicorn
* Git & GitHub

## Project Structure

```text
src/
├── core/
│   ├── config.py
│   └── security.py
│
├── db/
│   ├── database.py
│   └── session.py
│
├── schemas/
│   ├── auth.py
│   └── link.py
│
├── services/
│   ├── auth_service.py
│   └── link_service.py
│
├── routes/
│   ├── auth.py
│   └── links.py
│
├── utils/
│   └── helpers.py
│
├── main.py
│
requirements.txt
.env
README.md
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd save-links
```

### Create Virtual Environment

```bash
python -m venv myvenv
source myvenv/bin/activate
```

Windows:

```bash
myvenv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/savelinks
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run Database Migrations

```bash
alembic upgrade head
```

### Start Development Server

```bash
uvicorn src.main:app --reload
```

## API Documentation

After running the server:

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

## Planned Features

* Tags support
* Collections/Folders
* Browser extension
* Public and private links
* Link analytics
* Bookmark import/export
* URL metadata extraction
* Mobile application

## Goals

The goal of SaveLinks is to provide a fast, secure, and minimal bookmarking platform that helps users organize resources without relying on browser-specific bookmarks.

## License

This project is licensed under the MIT License.
