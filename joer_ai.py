import re
import random

class JoerAI:
    def __init__(self):
        self.patterns = [
            (r'\b(hi|hello|hey)\b', ['Hello!', 'Hi there!', 'Hey! How can I help you?']),
            (r'how are you', ['I'm doing well, thanks for asking!', 'I'm great! How about you?']),
            (r'what is your name', ['My name is JoerAI.', 'I'm JoerAI, nice to meet you!']),
            (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!']),
            (r'(\w+) (weather|temperature) (in|at) (\w+)', ['I'm sorry, I don\'t have access to real-time weather information.']),
            (r'tell me (about|something about) (\w+)', ['I\'m sorry, I don\'t have detailed information about {1}. Is there anything else I can help with?']),
            (r'what can you do', ['I can chat with you, answer simple questions, and try to help with basic tasks. What would you like to know?']),
        ]

    def respond(self, user_input):
        user_input = user_input.lower()
        for pattern, responses in self.patterns:
            match = re.search(pattern, user_input)
            if match:
                response = random.choice(responses)
                return response.format(*match.groups())
        return "I'm not sure how to respond to that. Can you please rephrase or ask something else?"

def main():
    joer = JoerAI()
    print("JoerAI: Hello! I'm JoerAI. How can I assist you today? (Type 'bye' to exit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("JoerAI: Goodbye! Have a great day!")
            break
        response = joer.respond(user_input)
        print("JoerAI:", response)

if __name__ == "__main__":
    main()
