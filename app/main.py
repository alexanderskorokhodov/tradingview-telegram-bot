from fastapi import FastAPI, Request
import logging
import json
from app.telegram import send_telegram_message

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.post("/webhook")
async def webhook_handler(request: Request):
    data = await request.json()
    message = data.get("message", json.dumps(data, indent=2))
    logging.info(f"Received alert: {message}")
    # Ensure the message is properly encoded
    safe_message = message.encode('utf-16', 'surrogatepass').decode('utf-16')
    await send_telegram_message(f"\U0001F4F1 *TradingView Alert*:\n```\n{safe_message}\n```")
    return {"status": "ok"} 