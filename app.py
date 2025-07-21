from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return "Chatbot is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")


    if "hello" in user_message.lower():
        reply = "Hi! How can I help you today?"
    else:
        reply = "A human agent will follow up soon."

    return jsonify({"response": reply})

if __name__ == "__main__":
     import os
     port = int(os.environ.get("PORT", 5000))
     app.run(host="0.0.0.0", port=port)
