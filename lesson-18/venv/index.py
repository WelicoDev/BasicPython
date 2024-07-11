import requests
from pprint import pprint

CHAT_ID = "<your_telegram_id>"
TOKEN = "<your_bot_token>"
your_message = input("message : ")
# API_URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={your_message}"
response = requests.get(API_URL)
pprint(response.json())