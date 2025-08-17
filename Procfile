web: gunicorn uptime_monitor.wsgi:application --bind 0.0.0.0:$PORT
worker: celery -A uptime_monitor worker --loglevel=info
beat: celery -A uptime_monitor beat --loglevel=info