import requests
import os
import sys

ACCESS_TOKEN = os.getenv("EAARb2dDZBO4oBPWtSZAqWYZCoe9prUVLOj6L4kjDW9JmrS7ctanlzATQsbTqw8fxAeVMdpIQ33kZA7Qu2ti5S6FTJvcsHemFiXnKAlsYZCTa5oWWWK2BZCNZBk6N2ZAgBlvZBuw34qZANp3tVsIPGMDeU5fT2KfmhaERlueDoanrQoyLpFPhWuZBPOg1HONROpJXpPT9BZBUkEa9mZAKNyI3ZCjQJ75kGRd8nSC3GhEmiW6I2QpFs3RQZDZD")
PHONE_NUMBER_ID = os.getenv("820817714447565")
RECIPIENT = os.getenv("+447928797754")

if not ACCESS_TOKEN or not PHONE_NUMBER_ID or not RECIPIENT:
    print("❌ Missing environment variables.")
    sys.exit(1)

MESSAGE = "Hello! This is your reminder 🚀"
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
    print("➡️ Sending request to:", URL)
    response = requests.post(URL, headers=HEADERS, json=data)
    print("✅ Response status:", response.status_code)
    print("📩 Response body:", response.text)

if __name__ == "__main__":
    send_whatsapp_message()
