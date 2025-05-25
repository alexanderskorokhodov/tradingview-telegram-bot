import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(var_name, prompt_text):
    """
    Retrieve an environment variable or prompt the user to input it if not found.

    Args:
        var_name (str): The name of the environment variable to retrieve.
        prompt_text (str): The text to prompt the user if the variable is not found.

    Returns:
        str: The value of the environment variable.
    """
    value = os.getenv(var_name)
    if not value:
        value = input(f"{prompt_text}: ")
        save_to_env_file(var_name, value)
    return value

def save_to_env_file(var_name, value):
    """
    Save a variable and its value to the .env file.

    Args:
        var_name (str): The name of the variable to save.
        value (str): The value of the variable to save.
    """
    with open('.env', 'a') as env_file:
        env_file.write(f"{var_name}={value}\n")

TELEGRAM_BOT_TOKEN = get_env_variable("TELEGRAM_BOT_TOKEN", "Enter your Telegram Bot Token")
TELEGRAM_CHAT_ID = get_env_variable("TELEGRAM_CHAT_ID", "Enter your Telegram Chat ID") 