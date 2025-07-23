from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Chatbot is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()

    if "refund" in user_message:
        reply = "Refunds are processed in 3 to 4 days."
    elif "order" in user_message:
        reply = "You can place an order here: https://wa.link/pks6oy"
    elif "cancel" in user_message:
        reply = "To cancel your order, use: https://wa.link/pks6oy"
    elif "delivery" in user_message or "how many days" in user_message:
        reply = "Your order will be delivered in 4 to 5 days."
    elif "products" in user_message or "what products" in user_message:
        reply = (
            "YuvaIOT offers a wide range of cutting-edge smart devices designed for homes, hotels, and industrial automation. Explore our collection of smart locks, intelligent lighting systems, voice-controlled assistants, energy-saving thermostats, air quality sensors, motion detectors, and smart surveillance cameras. "
            "Whether you are upgrading your living space, modernizing a hotel, or optimizing industrial safety and efficiency — we’ve got a solution that fits. Built with innovation and reliability, our products are here to make life easier, safer, and smarter."

        )
    elif "about" in user_message or "yuvaiot" in user_message:
        reply = (
            "YuvaIOT is an ecommerce platform providing innovative IoT products. "
            "We aim to simplify lives with smart automation for homes, hotels, and industries."
        )
    elif "contact" in user_message:
        reply = "Feel free to contact us here: https://wa.link/pks6oy"
    elif "hello" in user_message or "hi" in user_message:
        reply = "Hi! How can I help you today?"
    else:
        reply = "A human agent will follow up soon. Please contact us at https://wa.link/pks6oy for immediate assistance."

    return jsonify({"response": reply})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

