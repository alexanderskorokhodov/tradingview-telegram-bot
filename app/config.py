import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(var_name, prompt_text):
    value = os.getenv(var_name)
    if not value:
        value = input(f"{prompt_text}: ")
    return value

def save_to_env_file(var_name, value):
    with open('.env', 'a') as env_file:
        env_file.write(f"{var_name}={value}\n")

TELEGRAM_BOT_TOKEN = get_env_variable("TELEGRAM_BOT_TOKEN", "Enter your Telegram Bot Token")
if not os.getenv("TELEGRAM_BOT_TOKEN"):
    save_to_env_file("TELEGRAM_BOT_TOKEN", TELEGRAM_BOT_TOKEN)

TELEGRAM_CHAT_ID = get_env_variable("TELEGRAM_CHAT_ID", "Enter your Telegram Chat ID")
if not os.getenv("TELEGRAM_CHAT_ID"):
    save_to_env_file("TELEGRAM_CHAT_ID", TELEGRAM_CHAT_ID) 