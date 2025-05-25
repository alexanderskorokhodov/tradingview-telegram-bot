# TradingView Alert Webhook & Telegram Notifier

## Project Overview
This project receives webhooks from TradingView alerts and sends them to a Telegram group.

## Project Structure
```
project_root/
├── app/
│   ├── main.py              # FastAPI app
│   ├── telegram.py          # Telegram send logic
│   └── config.py            # Token & Chat ID settings
├── Dockerfile               # Docker container setup
└── requirements.txt         # Python dependencies
```

## Setup Instructions

### Prerequisites
- Docker
- Python 3.11

### Initial Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/tradingview-telegram-alerts.git
   cd tradingview-telegram-alerts
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Telegram credentials**
   - Create a `.env` file in the project root:
     ```plaintext
     TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
     TELEGRAM_CHAT_ID=YOUR_GROUP_CHAT_ID
     ```

### Docker Setup
1. **Build the Docker container**
   ```bash
   docker build -t tradingview-alert-bot .
   ```

2. **Run the container**
   ```bash
   docker run -d -p 8080:8080 --name alert-bot tradingview-alert-bot
   ```

3. [Optional] **Expose the service to the internet**
   - Use `ngrok` or configure DNS + HTTPS proxy:
     ```bash
     ngrok http 8080
     ```

### Environment Variables in Docker

You can manage your Telegram credentials in Docker using the following methods:

#### Option 1: Pass Environment Variables at Runtime

Run the Docker container with environment variables:

```bash
docker run -d -p 8080:8080 --name alert-bot \
  -e TELEGRAM_BOT_TOKEN=your_telegram_bot_token \
  -e TELEGRAM_CHAT_ID=your_telegram_chat_id \
  tradingview-alert-bot
```

#### Option 2: Use a `.env` File with Docker

1. Create a `.env` file in the project root with your credentials:

   ```plaintext
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

2. Run the Docker container using the `--env-file` option:

   ```bash
   docker run -d -p 8080:8080 --name alert-bot --env-file .env tradingview-alert-bot
   ```

#### Option 3: Build-time Environment Variables

Modify the `Dockerfile` to include build arguments and build the Docker image with build arguments:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY ./app /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

ARG TELEGRAM_BOT_TOKEN
ARG TELEGRAM_CHAT_ID

ENV TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN
ENV TELEGRAM_CHAT_ID=$TELEGRAM_CHAT_ID

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

Build the Docker image with build arguments:

```bash
docker build --build-arg TELEGRAM_BOT_TOKEN=your_telegram_bot_token \
             --build-arg TELEGRAM_CHAT_ID=your_telegram_chat_id \
             -t tradingview-alert-bot .
```

### TradingView Alerts Configuration
- **Webhook URL**: `