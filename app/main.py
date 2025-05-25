from fastapi import FastAPI, Request
import logging
import json
from .telegram import send_telegram_message

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.post("/webhook")
async def webhook_handler(request: Request):
    data = await request.json()
    message = data.get("message", json.dumps(data, indent=2))
    logging.info(f"Received alert: {message}")
    await send_telegram_message(f"\ud83d\udcf1 *TradingView Alert*:\n```\n{message}\n```")
    return {"status": "ok"} 