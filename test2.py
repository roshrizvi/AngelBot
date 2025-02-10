import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = os.getenv("TEST2_CHANNEL_ID")

def meow():
    """Sends an 'ANGEL' message to a Discord channel."""
    if not DISCORD_BOT_TOKEN or not CHANNEL_ID:
        print("Missing token or channel ID. Check your .env file.")
        return

    print("angel'd")

    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages"
    payload = {'content': 'ANGEL :pray: -b'}
    headers = {'Authorization': f'Bot {DISCORD_BOT_TOKEN}', 'Content-Type': 'application/json'}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for failed requests
        print(f"Message sent! Response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

    time.sleep(60)
