from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "Saim WhatsApp Agent is Running!"

@app.route('/api/index', methods=['POST','GET'])
def chat():
    data = request.json if request.is_json else {}
    msg = data.get('message', 'Hello')
    reply = f"Salam! Ap ne kaha: {msg}. Main Saim ka AI assistant hun."
    return jsonify({"reply": reply})
