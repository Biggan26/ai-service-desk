# AI Service Desk

# **Status:** 🚧 In Progress (Backend Engineering Training Project)



A backend REST API built with **FastAPI** as part of the GoML backend development training. This project demonstrates a clean project structure, database integration using SQLAlchemy, and basic CRUD operations.

## 🚀 Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Python 3.12

## Project Structure

```
ai-service-desk/
│── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── tests/
├── pyproject.toml
├── uv.lock
└── README.md
```

## ✅ Features Implemented

- Project setup using FastAPI
- Environment configuration with `.env`
- SQLite database integration
- SQLAlchemy ORM setup
- User model
- User schema validation using Pydantic
- Dependency Injection with FastAPI
- Service layer architecture
- Create User API (`POST /users`)
- Read All Users API (`GET /users`)

## 📌 Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health Check |
| POST | `/users` | Create a new user |
| GET | `/users` | Retrieve all users |

## ▶️ Run the Project

```bash
uv sync
uv run uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

## 📚 Learning Objective

This project is being developed as part of GoML backend engineering training to understand:

- FastAPI application architecture
- REST API development
- SQLAlchemy ORM
- Database session management
- Request validation with Pydantic
- Layered backend architecture (API → Service → Model → Database)

## 👨‍💻 Author

**G. M. Biggan**

Backend Engineering Training Project – GoML
