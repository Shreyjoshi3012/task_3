# chatbot.py

import nltk
import random
import string
import re

# ✅ Download NLTK resources (no try-except needed)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# 🧹 Preprocess user input
def preprocess(sentence):
    # Remove punctuation
    sentence = re.sub(f"[{re.escape(string.punctuation)}]", "", sentence)
    words = word_tokenize(sentence.lower())
    # Remove stopwords and lemmatize
    return [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

# 🧠 Knowledge base
raw_responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! Ask me anything.",
    "how are you": "I'm a bot, but I'm doing great! How about you?",
    "what is your name": "I am a simple chatbot built using Python and NLTK.",
    "bye": "Goodbye! Have a great day!",
    "help": "Sure! Ask me anything about weather, Python, or just say hi.",
    "what is weather like": "I'm sorry, I cannot provide real-time weather information.",
    "tell me about python": "Python is a high-level programming language known for simplicity.",
    "thank you": "You're welcome!",
    "thanks": "No problem!"
}

# ✅ Preprocess knowledge base keys
processed_responses = {preprocess(key): value for key, value in raw_responses.items()}

# 🔍 Matching logic
def respond(user_input):
    user_words = preprocess(user_input)

    if not user_words:
        return random.choice([
            "Please say something.",
            "I didn't catch that. Can you speak up?",
            "What can I help you with?"
        ])

    best_response = None
    max_matches = 0

    for key_words, response_text in processed_responses.items():
        current_matches = sum(1 for word in user_words if word in key_words)
        if current_matches > max_matches:
            max_matches = current_matches
            best_response = response_text

    if best_response and max_matches > 0:
        return best_response

    return random.choice([
        "I'm not sure I understand. Can you rephrase?",
        "Could you please elaborate?",
        "I'm still learning. Can you try asking in a different way?",
        "That's interesting, but I don't have an answer for that yet."
    ])

# 💬 Chat loop
print("🤖 ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("🧑 You: ")
    if user_input.lower() == 'bye':
        print("🤖 ChatBot:", raw_responses["bye"])
        break
    reply = respond(user_input)
    print("🤖 ChatBot:", reply)
