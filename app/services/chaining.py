from app.services.llm_provider import llm
from app.services.templates import prompt

chain = prompt | llm