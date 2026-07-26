![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![AWS Bedrock](https://img.shields.io/badge/AWS-Bedrock-orange)
![Pytest](https://img.shields.io/badge/Pytest-Testing-success)
![License](https://img.shields.io/badge/License-MIT-green)

# AI Service Desk  (Backend Engineering Training Project)

# **Status:** 🚧 Completed

# What i done ?
- FastAPI Application Development
- SQLAlchemy ORM
- PostgreSQL Database Integration
- RESTful API Design & Routing
- Database Relationships (Foundation)
- CRUD Operations (Create, Read, Update, Delete)
- Layered Architecture
- Service Layer Pattern
- Alembic Database Migration
- Middleware Implementation
- CORS Configuration
- Request Processing Time Middleware
- API Documentation using Swagger
- Pydantic Schema Validation
- AWS Bedrock AI Integration
- Health & Readiness Endpoints Check
- Unit Testing with Pytest
- Happy, Negative & Edge Case Testing
- Testing Coverage
- LOCUST Load Testing
- Profiling (cProfile + SnakeViz)
- cProfile result file save
- snakeviz Profile Graph
- Docker Containers
- Docker Images




## Screenshots
------

### Swagger API Documentation
![Swagger API](readme_picture_proof/Swagger%20API%20page1.png)
![Swagger API](readme_picture_proof/Swagger_API_page2.png)

----
## Testing Summary
1. Unit test - 20 passed
2. Integration Testing - 6 Passed
3. Total Test Cases - 26 Passed

--------
## Tests Coverage


![alt text](readme_picture_proof/test_case.png)

----
---


## Locust Load Test
1. NO Failures Found
![alt text](readme_picture_proof/locust.png)

----
## Alembic Migration for Database (PostgreSQL 18)

![alt text](readme_picture_proof/database_migration.png)

---

## Middleware Implementation & Request Processing Time

![alt text](readme_picture_proof/middleware_processing_time_check.png)

----


## Profiling (cProfile + SnakeViz) Graph
![alt text](readme_picture_proof/snakeviz_Profile_Graph.png)

-----

## Docker Container
![alt text](readme_picture_proof/Docker_Proof.png)


------

===========================================================

# AI Service Desk

An AI-powered Service Desk Backend built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Docker**, and **AWS Bedrock**. The system provides RESTful APIs for managing users and support tickets while integrating Generative AI to automatically summarize ticket descriptions.

---

## Project Overview

AI Service Desk is a backend application designed to simplify IT support ticket management through modern backend technologies and Generative AI.

The application provides a complete REST API for creating, updating, retrieving, and managing support tickets and users. In addition to standard CRUD operations, the system integrates Amazon Bedrock to generate intelligent summaries of ticket descriptions, helping support teams understand issues more efficiently.

The project follows a clean and modular architecture using FastAPI and SQLAlchemy, making the codebase easy to maintain, extend, and test. It also includes Docker support, database migration using Alembic, automated testing with Pytest, performance profiling, and load testing using Locust.

This project was developed as part of an AI Backend Engineering learning journey with a strong focus on production-ready backend development practices.

---

## Objectives

The primary objectives of this project are:

- Build a production-ready REST API using FastAPI.
- Manage users and support tickets efficiently.
- Integrate AWS Bedrock for AI-powered ticket summarization.
- Implement clean project architecture for maintainability.
- Use PostgreSQL as the primary relational database.
- Manage schema changes through Alembic migrations.
- Containerize the application using Docker.
- Ensure code quality through automated testing.
- Analyze application performance using profiling tools.
- Simulate concurrent users through load testing.

---

## Key Features

### User Management

- Create new users
- Retrieve all users
- Retrieve a specific user by ID

### Ticket Management

- Create support tickets
- Retrieve all tickets
- Retrieve ticket by ID
- Update ticket information
- Delete tickets

### AI Integration

- Summarize ticket descriptions using Amazon Bedrock
- Generate concise AI-powered summaries
- Support prompt-based text generation

### Health Monitoring

- Health Check endpoint
- Readiness endpoint

### Database

- PostgreSQL integration
- SQLAlchemy ORM
- Alembic database migrations

### Testing

- Unit Testing
- API Testing
- Integration Testing
- Performance Profiling
- Load Testing

### Deployment

- Docker containerization
- Docker Compose support
- Environment-based configuration

---

## Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.12 |
| Backend Framework | FastAPI |
| API Documentation | Swagger UI (OpenAPI) |
| ORM | SQLAlchemy 2.x |
| Database | PostgreSQL |
| Database Migration | Alembic |
| AI Service | AWS Bedrock |
| AWS SDK | Boto3 |
| Dependency Management | uv |
| Containerization | Docker |
| Container Orchestration | Docker Compose |
| Testing | Pytest |
| Performance Profiling | cProfile, SnakeViz |
| Load Testing | Locust |
| Version Control | Git & GitHub |

---

## Project Architecture

The project follows a layered architecture where each component has a dedicated responsibility.

```
                Client
                   │
                   ▼
          FastAPI API Layer
                   │
                   ▼
            Service Layer
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
SQLAlchemy ORM         AWS Bedrock
        │
        ▼
 PostgreSQL Database
```

### Architecture Flow

1. The client sends an HTTP request.
2. FastAPI receives and validates the request.
3. The appropriate Service processes the business logic.
4. SQLAlchemy communicates with PostgreSQL for database operations.
5. AI requests are forwarded to Amazon Bedrock.
6. The processed response is returned to the client.

---

## Project Structure

```text
AI-SERVICE-DESK
│
├── alembic/                       # Alembic migration scripts
│   ├── versions/                  # Database migration versions
│   ├── env.py                     # Alembic environment configuration
│   ├── script.py.mako             # Migration template
│   └── README                     # Alembic documentation
│
├── app/
│   ├── api/                       # API route definitions
│   ├── core/                      # Application configuration and settings
│   ├── database/                  # Database session and connection
│   ├── models/                    # SQLAlchemy ORM models
│   ├── schemas/                   # Pydantic request/response schemas
│   ├── services/                  # Business logic and AI services
│   ├── utils/                     # Shared utility functions
│   ├── __init__.py
│   └── main.py                    # FastAPI application entry point
│
├── tests/
│   ├── api/                       # API endpoint tests
│   ├── data/                      # Test datasets
│   ├── integration/               # Integration tests
│   ├── profile/                   # Performance profiling tests
│   ├── unit/                      # Unit tests
│   ├── __init__.py
│   └── conftest.py                # Shared pytest fixtures
│
├── readme_picture_proof/          # Screenshots used in README
│
├── .coverage                      # Code coverage report
├── .dockerignore                  # Files ignored during Docker build
├── .env.example                   # Sample environment variables
├── .gitignore                     # Git ignore rules
├── .python-version                # Python version configuration
├── alembic.ini                    # Alembic configuration
├── docker-compose.yml             # Docker Compose configuration
├── Dockerfile                     # Docker image definition
├── locustfile.py                  # Load testing configuration
├── pyproject.toml                 # Project metadata and dependencies
├── requirements.txt               # Exported Python dependencies
├── uv.lock                        # Locked dependency versions
├── README.md                      # Project documentation
└── ai_service_desk.db             # Local SQLite database (development only)
```

---

## Application Workflow

### User & Ticket Operations

```
Client Request
        │
        ▼
FastAPI Endpoint
        │
        ▼
Service Layer
        │
        ▼
SQLAlchemy ORM
        │
        ▼
PostgreSQL
        │
        ▼
JSON Response
```

---

### AI Ticket Summarization Workflow

```
Client Request
        │
        ▼
FastAPI Endpoint
        │
        ▼
AI Service
        │
        ▼
AWS Bedrock
        │
        ▼
Generated Summary
        │
        ▼
JSON Response
```

---

## API Modules

The application is divided into four primary API modules.

### Users API

Responsible for managing user-related operations.

- Create User
- Read Users
- Read User by ID

---

### Tickets API

Responsible for ticket lifecycle management.

- Create Ticket
- Read Tickets
- Read Ticket by ID
- Update Ticket
- Delete Ticket

---

### AI API

Provides AI-powered ticket summarization using Amazon Bedrock.

- Summarize Ticket

---

### Health API

Provides application health monitoring.

- Health Check
- Readiness Check

---


# Getting Started

This section explains how to set up and run the project from scratch. Follow the steps in the given order to avoid configuration issues.

---

## Prerequisites

Before running the project, make sure the following software is installed on your system.

| Software | Recommended Version |
|-----------|---------------------|
| Python | 3.12 or later |
| PostgreSQL | 16 or later |
| Git | Latest |
| Docker Desktop | Latest |
| Docker Compose | Latest |
| uv | Latest |

---

## Clone the Repository

Clone the project from GitHub.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory.

```bash
cd ai-service-desk
```

---

## Install Dependencies

This project uses **uv** as the dependency manager.

Install all required packages.

```bash
uv sync
```

If you need to install a new package later:

```bash
uv add package_name
```

Example:

```bash
uv add fastapi
```

---

## Environment Configuration

Create a new environment file.

```text
.env
```

You can copy the sample configuration.

```bash
cp .env.example .env
```

If you are using Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Update the values according to your environment.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/ai_service_desk

SECRET_KEY=your_secret_key

DEBUG=True

API_KEY=your_api_key

AWS_ACCESS_KEY_ID=your_access_key

AWS_SECRET_ACCESS_KEY=your_secret_key

AWS_REGION=us-east-1

AWS_DEMO_MODE=false

DATABASE_READY=true

BEDROCK_MODEL_ID=your_model_id
```

> **Important:** Never commit the `.env` file to GitHub because it contains sensitive credentials.

---

## Database Setup

Create a PostgreSQL database.

Example database name:

```text
ai_service_desk
```

Verify the database is created successfully.

Connect to PostgreSQL.

```bash
psql -U postgres
```

Switch to the database.

```sql
\c ai_service_desk
```

Display all tables.

```sql
\dt
```

Display all users.

```sql
SELECT * FROM users;
```

Display all tickets.

```sql
SELECT * FROM tickets;
```

---

# Database Migration

The project uses **Alembic** to manage database schema changes.

Initialize Alembic (Only required once).

```bash
uv run alembic init alembic
```

Generate a migration after updating SQLAlchemy models.

```bash
uv run alembic revision --autogenerate -m "Initial Schema"
```

Apply the migration to the database.

```bash
uv run alembic upgrade head
```

Check migration history.

```bash
uv run alembic history
```

Show the current migration version.

```bash
uv run alembic current
```

---

# Running the Application

## Development Mode

Start the FastAPI development server.

```bash
uv run uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```text
http://127.0.0.1:8000/redoc
```

OpenAPI JSON

```text
http://127.0.0.1:8000/openapi.json
```

---

## Verify the API

Open the health endpoint.

```text
GET /health
```

Example Response

```json
{
    "status": "healthy"
}
```

Check readiness.

```text
GET /ready
```

---

# Running with Docker

Build the Docker image.

```bash
docker compose build
```

Start all services.

```bash
docker compose up
```

Run in detached mode.

```bash
docker compose up -d
```

Verify running containers.

```bash
docker ps
```

View running logs.

```bash
docker compose logs
```

View live logs.

```bash
docker compose logs -f
```

Stop containers.

```bash
docker compose down
```

Rebuild everything.

```bash
docker compose up --build
```

---

## Access the Running Application

Application

```text
http://localhost:8000
```

Swagger UI

```text
http://localhost:8000/docs
```

Health Endpoint

```text
http://localhost:8000/health
```

Readiness Endpoint

```text
http://localhost:8000/ready
```

---

# Testing

Testing is an essential part of backend development. This project includes unit tests, API tests, integration tests, load testing, and performance profiling to ensure application reliability and maintainability.

---

## Project Test Structure

```text
tests/
│
├── api/                # API endpoint tests
├── integration/        # Integration tests
├── profile/            # Performance profiling
├── unit/               # Unit tests
├── data/               # Test data
└── conftest.py         # Shared pytest configuration
```

---

## Run All Tests

Execute every available test.

```bash
pytest -v
```

---

## Run Only Unit Tests

```bash
pytest tests/unit -v
```

---

## Run API Tests

```bash
pytest tests/api -v
```

---

## Run Integration Tests

```bash
pytest tests/integration -v
```

---

## Generate Test Coverage Report

```bash
pytest --cov=app tests
```

The coverage report shows how much of the application code is covered by automated tests.

---

# Performance Profiling

Performance profiling helps identify slow functions and performance bottlenecks.

---

## Run Performance Test

```bash
python tests/profile/profile_test.py
```

or

```bash
python -m tests.profile.profile_test
```

This command generates a profiling result file.

Example:

```text
profile_results.prof
```

---

## Visualize Profiling Results

```bash
snakeviz tests/profile/profile_results.prof
```

SnakeViz opens an interactive browser-based visualization of the profiling report, making it easier to identify time-consuming functions.

---

# Load Testing

The project uses **Locust** to simulate multiple concurrent users.

---

## Start Load Testing

```bash
locust -f locustfile.py
```

After starting Locust, open:

```text
http://localhost:8089
```

Configure:

- Number of Users
- Spawn Rate
- Host URL

Example:

```text
Host

http://localhost:8000
```

Run the simulation and monitor response times, throughput, and failures.

---

# Docker Command Reference

The following commands are frequently used while developing with Docker.

---

## Build Images

```bash
docker compose build
```

Builds the Docker image from the Dockerfile.

---

## Start Containers

```bash
docker compose up
```

Creates and starts all required containers.

---

## Run in Background

```bash
docker compose up -d
```

Runs containers in detached mode.

---

## Rebuild and Start

```bash
docker compose up --build
```

Rebuilds the image before starting containers.

---

## List Running Containers

```bash
docker ps
```

Displays all currently running containers.

---

## List All Containers

```bash
docker ps -a
```

Displays both running and stopped containers.

---

## View Logs

```bash
docker compose logs
```

Displays container logs.

---

## Follow Live Logs

```bash
docker compose logs -f
```

Continuously streams logs.

---

## Stop Containers

```bash
docker compose down
```

Stops and removes containers.

---

## Restart Containers

```bash
docker compose restart
```

Restarts all running containers.

---

## Remove Container

```bash
docker rm container_name
```

Removes a stopped container.

---

## Force Remove Container

```bash
docker rm -f container_name
```

Forcefully removes a running container.

---

## Remove Docker Images

```bash
docker rmi image_name
```

Deletes a Docker image.

---

## Execute Commands Inside a Container

```bash
docker exec -it container_name bash
```

Opens a shell inside the running container.

---

# PostgreSQL Cheat Sheet

Connect to PostgreSQL.

```bash
psql -U postgres
```

Connect to the project database.

```sql
\c ai_service_desk
```

List all databases.

```sql
\l
```

List all tables.

```sql
\dt
```

Describe a table.

```sql
\d users
```

Display all users.

```sql
SELECT * FROM users;
```

Display all tickets.

```sql
SELECT * FROM tickets;
```

Display the latest 10 tickets.

```sql
SELECT * FROM tickets ORDER BY id DESC LIMIT 10;
```

Exit PostgreSQL.

```sql
\q
```

---

# Useful Git Commands

Clone repository.

```bash
git clone <repository_url>
```

Check repository status.

```bash
git status
```

View modified files.

```bash
git diff
```

Stage all files.

```bash
git add .
```

Commit changes.

```bash
git commit -m "Your commit message"
```

Push changes.

```bash
git push origin main
```

Pull latest changes.

```bash
git pull origin main
```

View commit history.

```bash
git log --oneline
```

---

# Common Development Workflow

A typical development cycle follows these steps.

```text
1. Pull the latest code

↓

2. Create or switch to your feature branch

↓

3. Update models or business logic

↓

4. Generate Alembic migration (if database schema changes)

↓

5. Apply migration

↓

6. Run the application locally

↓

7. Test the API

↓

8. Execute automated tests

↓

9. Build Docker image

↓

10. Verify Docker execution

↓

11. Commit changes

↓

12. Push to GitHub
```

---

# Troubleshooting

This section contains the most common issues encountered during development and their solutions.

---

## Docker Container Name Already Exists

### Error

```text
Conflict. The container name is already in use.
```

### Solution

Remove the existing container.

```bash
docker rm -f ai-service-desk-api
```

Then start the application again.

```bash
docker compose up
```

---

## PostgreSQL Connection Refused

### Error

```text
sqlalchemy.exc.OperationalError
connection refused
```

### Possible Causes

- PostgreSQL service is not running.
- Invalid database credentials.
- Incorrect DATABASE_URL.
- Database does not exist.

### Solution

Verify that PostgreSQL is running.

Check your environment configuration.

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/ai_service_desk
```

If running inside Docker, verify the correct database host is being used.

---

## Alembic Migration Not Detected

### Possible Causes

- SQLAlchemy models were not imported.
- Metadata was not registered correctly.

### Solution

Verify that all models are imported before generating migrations.

Generate migration again.

```bash
uv run alembic revision --autogenerate -m "Updated Schema"
```

---

## Docker Build Failed

### Possible Causes

- Missing dependency
- Invalid Dockerfile
- Build cache issue

### Solution

Rebuild without cache.

```bash
docker compose build --no-cache
```

---

## Environment Variables Not Loaded

### Possible Causes

- Missing .env file
- Incorrect variable names
- Invalid environment configuration

### Solution

Verify that the .env file exists.

Check every variable carefully.

Restart the application after updating the environment.

---

## Swagger Page Not Opening

### Possible Causes

- Application is not running.
- Incorrect port mapping.
- FastAPI startup failed.

### Solution

Verify the running containers.

```bash
docker ps
```

Check logs.

```bash
docker compose logs -f
```

---

# Best Practices

This project follows several backend development best practices.

- Keep business logic inside the service layer.
- Separate models and schemas.
- Use SQLAlchemy ORM instead of raw SQL whenever possible.
- Store secrets inside environment variables.
- Never commit the `.env` file.
- Write tests before major refactoring.
- Generate Alembic migrations after every schema change.
- Keep Docker images lightweight.
- Use descriptive commit messages.
- Maintain clear API documentation.

---

# Security Notes

For security reasons:

- Never commit AWS credentials.
- Never commit API keys.
- Never commit database passwords.
- Never expose SECRET_KEY publicly.
- Keep `.env` inside `.gitignore`.
- Rotate AWS credentials if they are accidentally exposed.
- Use HTTPS in production.
- Store secrets using a secure secret management solution in production.

---

# Future Improvements

The current implementation provides a strong backend foundation. Future enhancements may include:

- JWT Authentication
- OAuth2 Authentication
- Role-Based Access Control (RBAC)
- Refresh Token Support
- Redis Caching
- Background Tasks
- Email Notifications
- File Upload Support
- Amazon S3 Integration
- Kubernetes Deployment
- CI/CD Pipeline
- GitHub Actions
- Centralized Logging
- Prometheus Metrics
- Grafana Dashboard
- API Rate Limiting
- Request Tracing
- OpenTelemetry
- WebSocket Notifications
- Multi-Tenant Support

---

# Learning Outcomes

This project helped strengthen practical knowledge in:

- FastAPI Development
- REST API Design
- SQLAlchemy ORM
- PostgreSQL
- Database Migration
- Docker Containerization
- Docker Compose
- Environment Configuration
- AWS Bedrock Integration
- Generative AI APIs
- Automated Testing
- Performance Profiling
- Load Testing
- Project Architecture
- Git and GitHub
- Backend Development Best Practices

---

# Useful Resources

## FastAPI

https://fastapi.tiangolo.com/

---

## SQLAlchemy

https://docs.sqlalchemy.org/

---

## Alembic

https://alembic.sqlalchemy.org/

---

## PostgreSQL

https://www.postgresql.org/docs/

---

## Docker

https://docs.docker.com/

---

## AWS Bedrock

https://docs.aws.amazon.com/bedrock/

---

## Pytest

https://docs.pytest.org/

---

## Locust

https://docs.locust.io/

---

## SnakeViz

https://jiffyclub.github.io/snakeviz/

---

# Contributing

Contributions are welcome.

If you find bugs or have ideas for improvements, feel free to open an issue or submit a pull request.

---


---

# Author

**G. M. Biggan**

Backend Developer | AI Enthusiast


---

# Thank You

Thank you for taking the time to explore this project.
