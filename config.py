import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
LANGUAGE = os.getenv("LANGUAGE", "pt")
SUPPORT_WHATSAPP = os.getenv("SUPPORT_WHATSAPP", "")

