from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8332167813:AAF4G8PIbbX_l-zZyUju1_bbt8pYLwDknFs"
CHAT_ID = "1103933621"

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
