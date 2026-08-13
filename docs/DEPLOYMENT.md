# Deployment

## Docker Compose
1. Copy `.env.example` to `.env`. 2. Replace all production credentials. 3. Run `docker compose up --build -d`. 4. Run migrations with `docker compose exec api alembic upgrade head`. 5. Verify `/health/ready` and `/metrics`.

## Production requirements
Use managed PostgreSQL/Redis, TLS termination, a secret manager, backups, centralized logs, network policies and an external monitoring stack. Do not expose database or Redis ports publicly.
