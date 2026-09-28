from langchain_openai import ChatOpenAI
from app.config import settings

llm = ChatOpenAI(
    model=settings.llm_model,
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=settings.llm_api_key,
)