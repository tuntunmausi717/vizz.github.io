import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Direct environment variable se uthao (no .env file needed)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash-exp')
chat = model.start_chat(history=[])

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    user_message = data.get('message', '')
    try:
        response = chat.send_message(
            f"Tu CHUT KA PYASA se baat kar raha hai. Hinglish mein jawab de, thoda mazak udate hue: {user_message}"
        )
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'reply': f'Error: {e}'})

@app.route('/')
def home():
    return "TUNTUNMAUSI KA BOT ZINDA HAI 😈🔥"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
