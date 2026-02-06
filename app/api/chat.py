from fastapi import APIRouter
from app.core.agent import RestaurantAgent

router = APIRouter()
agent = RestaurantAgent()

@router.post("/chat")
def chat(payload: dict):
    user_message = payload.get("message", "")
    response = agent.handle_message(user_message)
    return {"response": response}
