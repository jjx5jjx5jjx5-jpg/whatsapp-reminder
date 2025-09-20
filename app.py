import requests
import os
import sys
from datetime import datetime
import random

# Load secrets
ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
RECIPIENT = os.getenv("WHATSAPP_RECIPIENT")

# Exit if secrets missing
if not ACCESS_TOKEN or not PHONE_NUMBER_ID or not RECIPIENT:
    print("❌ Missing environment variables.")
    sys.exit(1)

# Define messages
MESSAGES = [
    "water. me so thirsty.",
    "gulps. hes behind me isnt he.",
    "think fast! water time1!",
    "you are so hydrated. no need to drink water",
    "My name is Lewis Warren and on the 14th June 2005..."
    "Hi Yas, it's me the god of water, Poseidon. you know what time it is"
    "Why did the glass of water cross the road?"
    "I think I'm getting shorter, I know you oughta, drink some water."
    "mii need a pepsi max"
    "it's 5 o clock somewhere. beer time!"
]

# Time window: only send between 07:30–22:00
now = datetime.now()
current_time = now.hour + now.minute / 60
if not (7.5 <= current_time <= 22):
    print("🕒 Outside allowed time window. Skipping.")
    sys.exit(0)

# Choose random message
MESSAGE = random.choice(MESSAGES)

# API call
URL = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def send_whatsapp_message():
    data = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT,
        "type": "text",
        "text": {"body": MESSAGE}
    }
    print("➡️ Sending:", MESSAGE)
    response = requests.post(URL, headers=HEADERS, json=data)
    print("✅ Status code:", response.status_code)
    print("📩 Response:", response.text)

if __name__ == "__main__":
    send_whatsapp_message()
