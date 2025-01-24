from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# OpenAI API Key - Set this in Render Environment Variables
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a friendly AI therapy chatbot."},
                  {"role": "user", "content": user_input}],
        temperature=0.9,
        max_tokens=250
    )

    return jsonify({"ai_response": response["choices"][0]["message"]["content"], "coping_strategy": "Try taking a deep breath!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
