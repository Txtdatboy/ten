import os

API_ID    = os.environ.get("API_ID", "20088962")
API_HASH  = os.environ.get("API_HASH", "257f47d347157555890a64b12bc0134f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6786890612:AAEvELybEXn_j4qGnQAFdB8m9JDkgMW9uXk") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
