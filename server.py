from flask import Flask, request, jsonify, render_template
from SentimentAnalysis.sentimet_analysis import generate_response
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask("app")

# Route to serve frontend
@app.route("/")
def home():
    return render_template("index.html")

# API route to handle chatbot interaction
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided."}), 400

    try:
        emotion, reply = generate_response(user_input)
        return jsonify({
            "emotion": emotion,
            "response": reply
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
