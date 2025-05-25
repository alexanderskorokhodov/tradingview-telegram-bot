import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(var_name, prompt_text):
    value = os.getenv(var_name)
    if not value:
        value = input(f"{prompt_text}: ")
        save_to_env_file(var_name, value)
    return value

def save_to_env_file(var_name, value):
    with open('.env', 'a') as env_file:
        env_file.write(f"{var_name}={value}\n")

TELEGRAM_BOT_TOKEN = get_env_variable("TELEGRAM_BOT_TOKEN", "Enter your Telegram Bot Token")
TELEGRAM_CHAT_ID = get_env_variable("TELEGRAM_CHAT_ID", "Enter your Telegram Chat ID") 