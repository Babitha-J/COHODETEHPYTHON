# chatbot.py
from flask import Flask, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

# Initialize Flask app
app = Flask(__name__)

# Define chatbot responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?", ]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.", ]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm feeling great!", ]
    ],
    [
        r"sorry (.*)",
        ["It's alright, don't worry.", "No problem.", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am an AI and I live in your computer.', ]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!", ]
    ],
]

# Create chatbot
chatbot = Chat(pairs, reflections)


# Root route
@app.route("/")
def home():
    return "Welcome to ChatBot! Ask me anything."


# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = chatbot.respond(user_message)
    return jsonify({"message": response})


if __name__ == "__main__":
    nltk.download("punkt")
    app.run(debug=True)
