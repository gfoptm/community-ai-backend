from contextlib import asynccontextmanager
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from prometheus_client import CONTENT_TYPE_LATEST,generate_latest
from app.core.config import settings
from app.core.errors import AppError,app_error_handler
from app.core.middleware import RequestContextMiddleware
from app.core.metrics import REQUESTS,LATENCY
from app.api.health import router as health_router
from app.api.routes import router as api_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    yield

s=settings()
app=FastAPI(title=s.app_name,version='1.0.0',docs_url='/docs' if s.docs_enabled else None,redoc_url='/redoc' if s.docs_enabled else None,lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=s.cors_origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
app.add_middleware(RequestContextMiddleware)
app.add_exception_handler(AppError,app_error_handler)

@app.middleware('http')
async def metrics_middleware(request:Request,call_next):
    path=request.url.path
    with LATENCY.labels(request.method,path).time(): response=await call_next(request)
    REQUESTS.labels(request.method,path,response.status_code).inc()
    return response

@app.get('/metrics',include_in_schema=False)
async def metrics():return Response(generate_latest(),media_type=CONTENT_TYPE_LATEST)
app.include_router(health_router)
app.include_router(api_router,prefix=s.api_prefix)
