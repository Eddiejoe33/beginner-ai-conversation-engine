# test_agent.py
from agent import ConversationAgent

# Initialize agent
agent = ConversationAgent()

# Predefined demo conversation
demo_messages = [
    "Hello",
    "Good morning",
    "I want to book an appointment",
    "Can you schedule it for tomorrow?",
    "Random text that doesn't match any intent",
    "Goodbye"
]

# Open log file to save conversation (optional, for demo purposes)
with open("conversation_log.txt", "w") as log_file:
    print("=== Professional Demo Conversation ===\n")
    log_file.write("=== Professional Demo Conversation ===\n\n")

    for msg in demo_messages:
        response = agent.get_response(msg)
        print(f"You: {msg}")
        print(f"Agent: {response}\n")
        log_file.write(f"You: {msg}\n")
        log_file.write(f"Agent: {response}\n\n")

    print("=== Demo Complete! Check conversation_log.txt for full log. ===")
    log_file.write("=== Demo Complete! ===\n")
