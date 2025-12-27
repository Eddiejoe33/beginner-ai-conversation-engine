INTENT_HANDLERS = {}

def greeting(user_input, context):
    return "Hello! How can I help you today?"

def appointment(user_input, context):
    context['appointment'] = True
    return "Sure! I can help you schedule an appointment."

# Register intents
INTENT_HANDLERS["greeting"] = greeting
INTENT_HANDLERS["appointment"] = appointment
