import nltk
from nltk.tokenize import word_tokenize
import random

nltk.download('punkt')

# Define intents and responses
intents = {
    "greeting": ["hi", "hello", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "farewell", "see you", "take care"],
    "thanks": ["thanks", "thank you", "thx"],
}

responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! Need any help?", "Hey! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Farewell!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "unknown": ["I'm sorry, I didn't understand that.", "Could you please rephrase?", "I'm not sure how to respond to that."],
}

def identify_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    for token in tokens:
        for intent, keywords in intents.items():
            if token in keywords:
                return intent
    return "unknown"

def get_response(intent):
    return random.choice(responses[intent])

def chat():
    print("Bot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break
        intent = identify_intent(user_input)
        response = get_response(intent)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()