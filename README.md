# EmoFelix API

A production-ready, API-only backend for an AI-based emotional support application, built with FastAPI.

## Features
- **JWT Authentication**: Secure login and registration.
- **User Profile Management**: Manage user data and preferences.
- **Membership & Payments**: Custom membership logic and payment handling.
- **Async Chat System**: Real-time, streaming chat with emotional AI model integration.
- **PostgreSQL + SQLAlchemy + Alembic**: Advanced async ORM and migrations.
- **Modular Structure**: Organized for scalability and maintainability.
- **Dockerized**: Easy local development and deployment.
- **.env Configuration**: Secure and flexible environment management.
- **GitHub Actions CI/CD**: Automated testing and deployment.
- **AWS Ready**: Configurable for cloud deployment.
- **API Docs**: Full OpenAPI docs at `/docs`.
- **Admin Routes**: Optional endpoints for user/session/payment management.

## API Routes

### Auth
- `POST   /api/auth/register` — Register a new user
- `POST   /api/auth/login` — Obtain JWT access token

### Users
- `GET    /api/users/me` — Get current user profile (JWT required)

### Payments
- `POST   /api/payments/create` — Create a payment (JWT required)
- `GET    /api/payments/my` — List current user's payments (JWT required)

### Chat & Sessions
- `POST   /api/chat/session/start` — Start a new chat session (JWT required)
- `POST   /api/chat/session/end/{session_id}` — End a chat session (JWT required)
- `POST   /api/chat/send` — Send a message in a session (JWT required)
- `GET    /api/chat/messages/{session_id}` — Get all messages in a session (JWT required)
- `POST   /api/chat/stream` — Stream AI emotional response (JWT required)

### Admin
- `GET    /api/admin/users` — List all users (admin JWT required)

## Request Body Examples

### Register
```json
POST /api/auth/register
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

### Login
```json
POST /api/auth/login (form-data)
{
  "username": "user@example.com",
  "password": "yourpassword"
}
```

### Create Payment
```json
POST /api/payments/create
{
  "user_id": 1,
  "amount": 9.99,
  "status": "pending"
}
```

### Send Chat Message
```json
POST /api/chat/send
{
  "session_id": 1,
  "sender": "user",
  "content": "I'm feeling stressed.",
  "emotion": "stressed"
}
```

### Stream AI Emotional Response
```json
POST /api/chat/stream
{
  "message": "I'm feeling stressed."
}
```

## Project Initialization & Startup

Follow these steps to initialize and start the project:

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd EmoFelix-API
   ```
2. **Create and activate a virtual environment (optional, for local Python development)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Copy and edit the environment file**
   ```bash
   cp .env .env.local  # or edit .env directly
   # Edit .env.local as needed
   ```
5. **Start PostgreSQL and the app using Docker Compose**
   ```bash
   docker-compose up --build
   ```
6. **Initialize the database with Alembic migrations**
   (In a new terminal, with Docker running)
   ```bash
   docker-compose exec web alembic upgrade head
   ```
7. **Access the API docs**
   [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Folder Structure
```
app/
  routers/      # API route definitions (APIRouter)
  models/       # SQLAlchemy models
  schemas/      # Pydantic schemas
  services/     # Business logic
  utils/        # Utility functions
  core/         # Core config, security, database
  migrations/   # Alembic migrations
```

## Quickstart
1. **Clone the repo**
2. **Configure `.env`**
3. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```
4. **Access API docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

## Deployment
- Ready for AWS ECS/Fargate or EC2.
- Configure secrets and environment variables for production.

## CI/CD
- GitHub Actions workflow for linting, testing, and deployment.

---

**Note:** This is a starter template. Implementations for authentication, chat, payments, and admin logic should be completed as per your requirements.