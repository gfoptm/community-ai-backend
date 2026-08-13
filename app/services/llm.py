from abc import ABC, abstractmethod
import httpx
from app.core.config import get_settings

class LLMProvider(ABC):
    @abstractmethod
    async def complete(self, prompt: str) -> str: ...

class MockLLMProvider(LLMProvider):
    async def complete(self, prompt: str) -> str:
        return f'Mock response: {prompt[:200]}'

class OpenAICompatibleProvider(LLMProvider):
    def __init__(self, api_key: str, model: str, base_url: str):
        self.api_key, self.model, self.base_url = api_key, model, base_url.rstrip('/')
    async def complete(self, prompt: str) -> str:
        if not self.api_key: raise RuntimeError('LLM_API_KEY is not configured')
        async with httpx.AsyncClient(timeout=60) as client:
            r=await client.post(f'{self.base_url}/chat/completions',headers={'Authorization':f'Bearer {self.api_key}'},json={'model':self.model,'messages':[{'role':'user','content':prompt}]})
            r.raise_for_status(); return r.json()['choices'][0]['message']['content']

def get_llm_provider() -> LLMProvider:
    s=get_settings()
    if s.llm_provider in {'openai','openai_compatible'}:
        return OpenAICompatibleProvider(s.llm_api_key,s.llm_model,s.llm_base_url)
    return MockLLMProvider()
