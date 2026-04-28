from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__)
CORS(app)

# Groq client setup
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL_NAME = "llama-3.3-70b-versatile"

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    user_message = data.get('message', '')
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Tu ek mastikhor Hinglish AI assistant hai. Tera kaam hai CHUTTADBHUDDI naam ke user ki Hinglish mein help karna aur thoda mazak udana. Hamesha 'CHUTTADBHUDDI' kahkar baat karna."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model=MODEL_NAME,
        )
        
        reply = chat_completion.choices[0].message.content
        return jsonify({'reply': reply})
        
    except Exception as e:
        return jsonify({'reply': f'Error: {str(e)}'})

@app.route('/')
def home():
    return "OGGY BHAI KA BOT ZINDA HAI 😈🔥"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
