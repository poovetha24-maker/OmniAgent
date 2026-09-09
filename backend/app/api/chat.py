from fastapi import APIRouter
from backend.app.models.chat_models import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        response=f"OmniAgent received: {request.message}"
    )