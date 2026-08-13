from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class ErrorBody(BaseModel):
    code:str
    message:str
    request_id:str|None=None

class AppError(Exception):
    def __init__(self,code:str,message:str,status_code:int=400):
        self.code=code; self.message=message; self.status_code=status_code

async def app_error_handler(request:Request,exc:AppError):
    return JSONResponse(status_code=exc.status_code,content=ErrorBody(code=exc.code,message=exc.message,request_id=getattr(request.state,'request_id',None)).model_dump())
