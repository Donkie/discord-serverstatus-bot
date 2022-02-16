
import os

from Client import Client

print("Starting discord-serverstatus-bot")

BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_SERVER_TYPE = os.getenv('BOT_SERVER_TYPE')
BOT_SERVER_IP = os.getenv('BOT_SERVER_IP')
BOT_SERVER_PORT = int(os.getenv('BOT_SERVER_PORT'))

print(f"Token: {BOT_TOKEN}")
print(f"Server type: {BOT_SERVER_TYPE}")
print(f"Server address: {BOT_SERVER_IP}:{BOT_SERVER_PORT}")

client = Client(type = BOT_SERVER_TYPE, ipport = (BOT_SERVER_IP, BOT_SERVER_PORT))
client.run(BOT_TOKEN)
