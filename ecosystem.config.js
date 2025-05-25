module.exports = {
  apps: [
    {
      name: "TV-Alerts",
      script: "uvicorn",
      args: "app.main:app --host 0.0.0.0 --port 80",
      interpreter: "none"
    }
  ]
} 