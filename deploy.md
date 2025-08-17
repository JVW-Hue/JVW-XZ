# 🚀 Deployment Guide

## Quick Deploy Options

### 1. Heroku (Recommended)
```bash
# Install Heroku CLI
heroku create your-app-name
heroku addons:create heroku-postgresql:mini
heroku addons:create heroku-redis:mini

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
heroku config:set PAYPAL_CLIENT_ID=ARK6NTOx6BYynt7sXT2RXr5L1Wkus7MRwIVRXKdBq-ngBWxcg8q1IR-sRM8oui_wZUMdgAIjLtcpal79

# Deploy
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
```

### 2. Railway
1. Connect GitHub repo to Railway
2. Add PostgreSQL and Redis services
3. Set environment variables
4. Deploy automatically

### 3. Render
1. Connect GitHub repo
2. Add PostgreSQL and Redis
3. Configure environment variables
4. Deploy

## Environment Variables Needed
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
PAYPAL_CLIENT_ID=ARK6NTOx6BYynt7sXT2RXr5L1Wkus7MRwIVRXKdBq-ngBWxcg8q1IR-sRM8oui_wZUMdgAIjLtcpal79
DATABASE_URL=postgres://...
REDIS_URL=redis://...
```

## Post-Deployment
1. Run migrations: `python manage.py migrate`
2. Create superuser: `python manage.py createsuperuser`
3. Collect static files: `python manage.py collectstatic`
4. Start Celery worker and beat for monitoring

Your app is production-ready! 🎉