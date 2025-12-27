from agent import ConversationAgent

def run_demo():
    agent = ConversationAgent()
    print("Welcome to the Beginner AI Conversation Engine!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = agent.process_input(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    run_demo()
