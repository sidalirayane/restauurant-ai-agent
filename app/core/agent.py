class RestaurantAgent:
    def handle_message(self, message: str) -> str:
        message = message.lower()

        if "heure" in message or "horaire" in message:
            return "Le restaurant est ouvert de 11h à 23h."

        if "menu" in message or "pizza" in message:
            return "Nous proposons plusieurs pizzas, classiques et spéciales."

        return (
            "Je peux vous aider pour les horaires, le menu "
            "ou vous transférer à un employé."
        )
