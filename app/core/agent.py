from app.core.intents import INTENTS


def handle_message(message: str) -> str:
    msg = message.lower()

    for intent, data in INTENTS.items():
        if any(keyword in msg for keyword in data["keywords"]):
            return data["response"]

    return "🤖 Désolé, je n’ai pas compris votre demande."
