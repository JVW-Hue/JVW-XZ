# 🌐 UptimeGuard - Website Monitoring SaaS

A modern, scalable SaaS application for monitoring website uptime with real-time alerts, beautiful dashboards, and PayPal payment integration.

## ✨ Features

- **Real-time Monitoring**: Track website uptime and performance
- **Beautiful Dashboard**: Modern UI with stunning glass morphism design
- **User Authentication**: Secure signup/login system
- **Website Management**: Add, view, and monitor multiple websites
- **PayPal Integration**: Premium and Pro subscription plans
- **Responsive Design**: Works perfectly on all devices
- **Production Ready**: Deployed on Render with PostgreSQL

## 🚀 Live Demo

**Production URL:** https://jvw-xz.onrender.com

## 🛠️ Tech Stack

- **Backend:** Django 4.2.7
- **Database:** PostgreSQL (Production), SQLite (Local)
- **Frontend:** TailwindCSS, Font Awesome
- **Payments:** PayPal REST API
- **Deployment:** Render
- **Storage:** WhiteNoise for static files

## 📦 Installation

### Local Development

1. **Clone Repository**
   ```bash
   git clone https://github.com/JVW-Hue/JVW-XZ.git
   cd JVW-XZ
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start Server**
   ```bash
   python manage.py runserver
   ```

5. **Access Application**
   - Local: http://127.0.0.1:8000
   - Create account and start monitoring!

## 🌍 Deployment

### Render (Current)
- Automatic deployment from GitHub
- PostgreSQL database included
- SSL certificate provided
- Custom domain support

### Environment Variables
```env
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://...
PAYPAL_CLIENT_ID=your-paypal-client-id
PAYPAL_CLIENT_SECRET=your-paypal-secret
```

## 💰 Pricing Plans

- **Free**: Basic monitoring features
- **Premium ($9/mo)**: Enhanced monitoring, faster checks
- **Pro ($19/mo)**: Unlimited websites, SMS alerts, priority support

## 🎨 Design Features

- Glass morphism UI design
- Gradient backgrounds
- Floating animations
- Responsive layouts
- Modern typography
- Professional color schemes

## 📱 Screenshots

- Beautiful landing page with call-to-action
- Stunning signup/login forms
- Professional dashboard with statistics
- Detailed website monitoring views
- PayPal payment integration

## 🔒 Security

- CSRF protection enabled
- Secure headers configured
- SSL/HTTPS ready
- Input validation
- SQL injection prevention

## 🚀 Performance

- Optimized database queries
- Static file compression
- CDN-ready assets
- Efficient caching
- Fast response times

## 📊 Monitoring Features

- Website uptime tracking
- Response time monitoring
- Status change alerts
- Historical data
- Performance analytics

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details

## 🆘 Support

- **Live App:** https://jvw-xz.onrender.com
- **GitHub:** https://github.com/JVW-Hue/JVW-XZ
- **Issues:** Create GitHub issue for support

---

**Built with ❤️ using Django, TailwindCSS, and modern web technologies**

🌟 **Star this repo if you found it helpful!**