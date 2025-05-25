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
├── ecosystem.config.js      # PM2 ecosystem file
├── requirements.txt         # Python dependencies
└── .gitignore               # Git ignore file
```

## Setup Instructions

### Prerequisites
- Python 3.11
- Node.js and npm (for PM2)

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

### Running with PM2

PM2 can be used to manage the FastAPI application, providing features like process management and monitoring.

1. **Install PM2** (if not already installed):
   ```bash
   npm install pm2 -g
   ```

2. **Start the application using PM2**:
   ```bash
   pm2 start ecosystem.config.js
   ```

3. **Check the status of the application**:
   ```bash
   pm2 status
   ```

4. **View logs**:
   ```bash
   pm2 logs TV-Alerts
   ```

5. **Stop the application**:
   ```bash
   pm2 stop TV-Alerts
   ```

6. **Restart the application**:
   ```bash
   pm2 restart TV-Alerts
   ```

### TradingView Alerts Configuration

- **Webhook URL**: `http://yourdomain.com/webhook`
- **Message**: `{"message":"{{strategy.order.alert_message}}"}`

## License
This project is licensed under the MIT License.

## Repository

You can find the project repository on GitHub at the following link: [tradingview-telegram-bot](https://github.com/alexanderskorokhodov/tradingview-telegram-bot)

## Additional Setup Instructions

### Environment Setup
- Ensure that the `.env` file is correctly set up with your Telegram credentials.
- The `env/` directory is used for the Python virtual environment. Ensure it is activated before running the application.

### Running Tests
- If there are any tests, describe how to run them here.

### Additional Tools
- Mention any additional tools or scripts that are part of the project.