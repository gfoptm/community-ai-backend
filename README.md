# Community AI Backend — v1.0.0

Free MIT-licensed FastAPI foundation for production-oriented AI services. Use it as the public/community edition and upgrade path into the paid RAG/Agent and SaaS products.

## Included
- FastAPI `/api/v1` contract with interactive OpenAPI docs.
- Mock and OpenAI-compatible LLM provider abstraction.
- Async PostgreSQL and Redis configuration.
- Liveness/readiness endpoints, request IDs, security headers and Prometheus metrics.
- Alembic release workflow, Docker Compose, non-root container and CI.
- Tests, security policy, contribution guide and deployment runbook.

## Quick start
```bash
cp .env.example .env
docker compose up --build -d
# API: http://localhost:8000/docs
# liveness: http://localhost:8000/health/live
```
For local Python development: `pip install -e '.[dev]' && uvicorn app.main:app --reload`.

## Production note
The project is a foundation, not a compliance/security certification. Use managed data stores, TLS, secret management, backups and centralized monitoring in real deployments. See `docs/DEPLOYMENT.md`.

## License
MIT — see `LICENSE`.
