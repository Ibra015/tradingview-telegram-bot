from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = ""
CHAT_ID = ""

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=payload)

@app.route('/tv', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get('message', str(data))
    send_telegram(message)
    return {"ok": True}

if __name__ == "__main__":
    app.run()

