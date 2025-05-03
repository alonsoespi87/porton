from utils.db_utils import get_menu

def generate_response(intent):
    if intent == "greeting":
        return "Hi, welcome to Café Portón. What would you like to order?"
    elif intent == "ask_menu":
        menu = get_menu()
        return "We offer: " + ", ".join(f"{item[0]} for {item[1]} pesos" for item in menu)
    elif intent == "thanks":
        return "You're welcome! Let me know if you need anything else."
    elif intent == "goodbye":
        return "Goodbye! Thanks for visiting."
    elif intent == "order_drink":
        return "Sure! What size would you like?"
    else:
        return None
