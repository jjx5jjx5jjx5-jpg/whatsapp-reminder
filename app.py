import requests
import os
import sys

# Load secrets from environment variables
ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
RECIPIENT = os.getenv("WHATSAPP_RECIPIENT")

# Exit if any secret is missing
if not ACCESS_TOKEN or not PHONE_NUMBER_ID or not RECIPIENT:
    print("❌ Missing environment variables. Check your GitHub secrets.")
    sys.exit(1)

# Your reminder message
MESSAGE = "Hello! This is your automated reminder 🚀"

# WhatsApp Cloud API URL
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
    print("➡️ Sending WhatsApp message...")
    response = requests.post(URL, headers=HEADERS, json=data)
    print("✅ Status code:", response.status_code)
    print("📩 Response:", response.text)

if __name__ == "__main__":
    send_whatsapp_message()
