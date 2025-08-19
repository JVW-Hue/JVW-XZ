#!/usr/bin/env python
import os
import sys
import django
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uptime_monitor.settings')
    django.setup()
    
    # Start server on port 8001
    sys.argv = ['manage.py', 'runserver', '127.0.0.1:8001']
    execute_from_command_line(sys.argv)