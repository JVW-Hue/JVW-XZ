# 🌐 Website Uptime Monitor SaaS

A modern, scalable SaaS application for monitoring website uptime with real-time alerts, beautiful dashboards, and public status pages.

## ✨ Features

- **Real-time Monitoring**: Check websites every 30 seconds to 5 minutes
- **Instant Alerts**: Email and SMS notifications when sites go down
- **Beautiful Dashboard**: Modern UI with real-time updates via WebSockets
- **Public Status Pages**: Custom status pages for transparency
- **Subscription Plans**: Freemium model with Stripe integration
- **Scalable Architecture**: Built with Django, Celery, and Redis

## 🚀 Quick Start

### Local Development

1. **Clone and Setup**
   ```bash
   git clone <your-repo>
   cd uptime-monitor
   pip install -r requirements.txt
   ```

2. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run Services**
   ```bash
   # Terminal 1: Django
   python manage.py runserver
   
   # Terminal 2: Celery Worker
   celery -A uptime_monitor worker --loglevel=info
   
   # Terminal 3: Celery Beat
   celery -A uptime_monitor beat --loglevel=info
   ```

### Docker Development

```bash
docker-compose up --build
```

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Django Web    │    │  Celery Worker  │    │  Celery Beat    │
│   (Frontend)    │    │  (Monitoring)   │    │  (Scheduler)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
         ┌─────────────────┐    ┌─────────────────┐
         │   PostgreSQL    │    │     Redis       │
         │   (Database)    │    │  (Task Queue)   │
         └─────────────────┘    └─────────────────┘
```

## 💰 Pricing Model

- **Free**: 1 website, 5-minute checks, email alerts
- **Premium ($9/mo)**: 5 websites, 1-minute checks, reports
- **Pro ($19/mo)**: Unlimited websites, 30s checks, SMS alerts, status pages

## 🌍 Deployment Options

### 1. Heroku (Recommended for MVP)
```bash
# Install Heroku CLI
heroku create your-app-name
heroku addons:create heroku-postgresql:mini
heroku addons:create heroku-redis:mini
heroku config:set SECRET_KEY=your-secret-key
git push heroku main
```

### 2. Railway
```bash
# Connect GitHub repo to Railway
# Add PostgreSQL and Redis services
# Deploy automatically on push
```

### 3. Render
```bash
# Connect GitHub repo
# Add PostgreSQL and Redis
# Configure environment variables
```

### 4. DigitalOcean App Platform
```bash
# Connect GitHub repo
# Add managed database and Redis
# Configure auto-deploy
```

## 🔧 Configuration

### Required Environment Variables

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com

# Database
DB_NAME=uptime_monitor
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379/0

# Email (SendGrid)
SENDGRID_API_KEY=your-sendgrid-key

# SMS (Twilio)
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token

# Payments (Stripe)
STRIPE_PUBLISHABLE_KEY=pk_live_your-key
STRIPE_SECRET_KEY=sk_live_your-key
STRIPE_WEBHOOK_SECRET=whsec_your-secret
```

## 📊 Monitoring & Analytics

- **Uptime Percentage**: 24h, 7d, 30d tracking
- **Response Time**: Average and historical data
- **Incident Management**: Automatic detection and resolution
- **Real-time Updates**: WebSocket-powered dashboard

## 🔒 Security Features

- CSRF protection
- SQL injection prevention
- XSS protection
- Secure headers
- Rate limiting (add django-ratelimit)

## 🚀 Scaling Considerations

### Performance Optimizations
- Database indexing on frequently queried fields
- Redis caching for dashboard data
- CDN for static assets
- Database connection pooling

### Horizontal Scaling
- Multiple Celery workers
- Load balancer for web servers
- Database read replicas
- Redis clustering

## 📈 Marketing & Growth

### Launch Strategy
1. **Product Hunt**: Launch for initial visibility
2. **Content Marketing**: Blog about website monitoring
3. **SEO**: Target "website monitoring" keywords
4. **Social Media**: Share downtime horror stories
5. **Partnerships**: Integrate with hosting providers

### Pricing Strategy
- Freemium to attract users
- Clear upgrade path
- Annual discounts
- Enterprise plans for larger customers

## 🛠️ Development Roadmap

### Phase 1 (MVP) ✅
- [x] User authentication
- [x] Website monitoring
- [x] Email alerts
- [x] Basic dashboard
- [x] Stripe integration

### Phase 2
- [ ] SMS alerts
- [ ] Public status pages
- [ ] API access
- [ ] Team accounts
- [ ] Custom check intervals

### Phase 3
- [ ] Multi-location monitoring
- [ ] Keyword monitoring
- [ ] SSL certificate monitoring
- [ ] Performance monitoring
- [ ] Integrations (Slack, Discord, Webhooks)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

- Documentation: [docs.yourapp.com]
- Email: support@yourapp.com
- Discord: [Your Discord Server]

---

**Built with ❤️ using Django, Celery, and modern web technologies**