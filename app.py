import os
import secrets
from flask import Flask, request, jsonify, render_template, session
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 1024,
    },
    safety_settings=[
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ],
    system_instruction="You are Quinn, a helpful and concise AI assistant. Answer clearly and accurately."
)


def get_chat():
    """Return a per-session chat instance."""
    if "history" not in session:
        session["history"] = []
    return model.start_chat(history=session["history"])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        chat = get_chat()
        response = chat.send_message(user_input)
        # Persist updated history back to session
        session["history"] = [
            {"role": m.role, "parts": [p.text for p in m.parts]}
            for m in chat.history
        ]
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/reset", methods=["POST"])
def reset():
    session.pop("history", None)
    return jsonify({"status": "conversation reset"})


if __name__ == "__main__":
    app.run(debug=False)
