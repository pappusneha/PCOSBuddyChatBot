from fastapi import FastAPI
from app.chatbot import get_response
from app.models import ChatRequest, ChatResponse

app = FastAPI(title="PCOSBuddy Chatbot")

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    user_message = request.message
    response = get_response(user_message)
    return ChatResponse(response=response)