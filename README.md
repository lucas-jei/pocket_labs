# FastAPI Web Backend Template (DB + Auth)

This template provides a practical starter structure for a FastAPI web-service backend with:
- Async SQLAlchemy (2.x) + PostgreSQL (asyncpg)
- Alembic migrations
- JWT auth (access token) scaffolding (refresh can be added later)

## Quickstart

1) Create and activate a virtualenv, then install deps:
```bash
pip install -r requirements.txt
```

2) Create `.env` (copy from `.env.example`) and set values.

3) Run the API:
```bash
uvicorn app.main:app --reload
```

4) API docs:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Alembic (migrations)

Initialize DB first (Postgres recommended), then run:
```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```

> Note: Alembic autogenerate needs `app/db/base.py` to import all models.
