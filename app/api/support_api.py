from fastapi import APIRouter
from app.services.chaining import chain
from app.services.tools import llm_with_tools,TOOL_MAP
from pydantic import BaseModel

router = APIRouter(prefix='/support')

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def ask_support(request: ChatRequest):
    print(">step 0.....")

    response = llm_with_tools.invoke(
        request.message
    )
    print(">step 1.....")
    tool_call = response.tool_calls[0]

    print(tool_call["name"])
    print(tool_call["args"])
    function = tool_call["name"]
    argument = tool_call["args"]
    if not TOOL_MAP.get(function):
        return {
            "answer": "Function could not find"
        }
    tool = TOOL_MAP.get(function)
    result = tool.invoke(
                tool_call["args"]
            )

    return {
        "answer": result
    }

