from flask import Flask, request, render_template_string
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

app = Flask(__name__)

def identify_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    for token in tokens:
        for intent, keywords in intents.items():
            if token in keywords:
                return intent
    return "unknown"

def get_response(intent):
    return random.choice(responses[intent])

html_template = """
<!doctype html>
<html lang='en'>
  <head>
    <title>Chatbot</title>
    <style>
      body {{ font-family: Arial, sans-serif; margin: 50px; }}
      .chatbox {{ width: 500px; margin: auto; }}
      input[type=text] {{ width: 80%; padding: 10px; }}
      input[type=submit] {{ padding: 10px; }}
      .messages {{ margin-top: 20px; }}
      .user, .bot {{ margin: 10px 0; }}
      .user {{ color: blue; }}
      .bot {{ color: green; }}
    </style>
  </head>
  <body>
    <div class="chatbox">
      <h1>Simple AI Chatbot</h1>
      <form action="/chat" method="post">
        <input type="text" name="message" autofocus required>
        <input type="submit" value="Send">
      </form>
      <div class="messages">
        {% if user_message %}
          <div class="user"><strong>You:</strong> {{ user_message }}</div>
          <div class="bot"><strong>Bot:</strong> {{ bot_response }}</div>
        {% endif %}
      </div>
    </div>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(html_template, user_message=None, bot_response=None)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    intent = identify_intent(user_message)
    bot_response = get_response(intent)
    return render_template_string(html_template, user_message=user_message, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)