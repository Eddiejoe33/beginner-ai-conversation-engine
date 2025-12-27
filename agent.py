# agent.py
from intents import INTENT_HANDLERS
from fallback import handle_fallback

class ConversationAgent:
    """
    Professional AI Conversation Agent
    Handles greetings, appointments, fallback responses, and context.
    """

    def __init__(self):
        self.context = {}

    def process_input(self, user_input):
        """
        Process user input and return the agent's response.
        """
        intent = self.classify_intent(user_input)
        handler = INTENT_HANDLERS.get(intent)

        if handler:
            response = handler(user_input, self.context)
        else:
            response = handle_fallback(user_input, self.context)

        return response

    def classify_intent(self, user_input):
        """
        Simple keyword-based intent classification.
        """
        user_input = user_input.lower()
        if any(greet in user_input for greet in ["hello", "hi", "good morning", "good afternoon"]):
            return "greeting"
        elif any(book in user_input for book in ["appointment", "book", "schedule"]):
            return "appointment"
        else:
            return "unknown"

    def get_response(self, user_input):
        """
        Beginner-friendly method for test scripts or demos.
        """
        return self.process_input(user_input)
