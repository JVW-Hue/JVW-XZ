# 🌐 UptimeGuard - Website Monitoring App

A Django web application for real-time website uptime monitoring.

## ✨ Features

- Real-time website monitoring
- Live status indicators (online/offline)
- Response time tracking
- Uptime percentage calculation
- User authentication
- Beautiful dashboard

## 🛠️ Tech Stack

- Django 4.2.7
- PostgreSQL (Production) / SQLite (Local)
- TailwindCSS
- WhiteNoise for static files

## 🚀 Deploy to Production

### Railway (Recommended)
1. Fork this repository
2. Go to [Railway](https://railway.app)
3. Connect your GitHub account
4. Deploy from your forked repository
5. Add environment variables (see .env.example)

### Heroku
1. Install Heroku CLI
2. `heroku create your-app-name`
3. `git push heroku main`
4. `heroku run python manage.py migrate`

## 📦 Local Development

```bash
git clone https://github.com/JVW-Hue/JVW-XZ.git
cd JVW-XZ
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🎯 Usage

1. Sign up for an account
2. Add websites to monitor
3. Click "Check Now" to test status
4. View real-time uptime data