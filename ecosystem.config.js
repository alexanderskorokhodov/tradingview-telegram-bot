module.exports = {
  apps: [
    {
      name: "alert-bot",
      script: "uvicorn",
      args: "app.main:app --host 0.0.0.0 --port 8080",
      interpreter: "none"
    }
  ]
} 