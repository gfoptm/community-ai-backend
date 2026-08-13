from fastapi import APIRouter,Response,status
router=APIRouter(tags=['health'])

@router.get('/health/live')
async def live():return {'status':'ok'}

@router.get('/health/ready')
async def ready(response:Response):
    checks={}
    try:
        from sqlalchemy import text
        from app.db.session import engine
        async with engine.connect() as conn: await conn.execute(text('SELECT 1'))
        checks['database']='ok'
    except Exception: checks['database']='unavailable'
    try:
        import redis.asyncio as redis
        from app.core.config import settings
        client=redis.from_url(settings().redis_url,decode_responses=True); await client.ping(); await client.aclose(); checks['redis']='ok'
    except Exception: checks['redis']='unavailable'
    ok=all(v=='ok' for v in checks.values())
    if not ok: response.status_code=status.HTTP_503_SERVICE_UNAVAILABLE
    return {'status':'ok' if ok else 'degraded','checks':checks}
