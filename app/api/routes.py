from fastapi import APIRouter, Depends
from app.api.schemas import ChatRequest, ChatResponse
from app.services.llm import LLMProvider, get_llm_provider
router = APIRouter()
@router.post('/chat', response_model=ChatResponse)
async def chat(payload: ChatRequest, llm: LLMProvider = Depends(get_llm_provider)) -> ChatResponse:
    return ChatResponse(answer=await llm.complete(payload.message))
