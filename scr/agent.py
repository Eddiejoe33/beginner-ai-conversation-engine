from intents import INTENT_HANDLERS
from fallback import handle_fallback

class ConversationAgent:
    def __init__(self):
        self.context = {}

    def process_input(self, user_input):
        # Simple keyword-based intent detection
        intent = self.classify_intent(user_input)
        handler = INTENT_HANDLERS.get(intent)

        if handler:
            response = handler(user_input, self.context)
        else:
            response = handle_fallback(user_input, self.context)

        return response

    def classify_intent(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input or "hi" in user_input:
            return "greeting"
        elif "appointment" in user_input or "book" in user_input:
            return "appointment"
        else:
            return "unknown"
