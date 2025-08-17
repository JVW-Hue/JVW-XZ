from celery.schedules import crontab
from uptime_monitor.apps.monitoring.tasks import schedule_all_checks

CELERYBEAT_SCHEDULE = {
    'check-all-websites': {
        'task': 'uptime_monitor.apps.monitoring.tasks.schedule_all_checks',
        'schedule': crontab(minute='*'),  # Run every minute
    },
}