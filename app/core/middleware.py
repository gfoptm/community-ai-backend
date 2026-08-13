import time, uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request,call_next):
        request.state.request_id=request.headers.get('x-request-id') or str(uuid.uuid4())
        start=time.perf_counter()
        response:Response=await call_next(request)
        response.headers['x-request-id']=request.state.request_id
        response.headers['x-response-time-ms']=f'{(time.perf_counter()-start)*1000:.2f}'
        response.headers['x-content-type-options']='nosniff'
        response.headers['x-frame-options']='DENY'
        response.headers['referrer-policy']='no-referrer'
        return response
