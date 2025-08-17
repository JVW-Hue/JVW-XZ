#!/usr/bin/env python3
"""
Setup script for Website Uptime Monitor SaaS
Run this script to set up the development environment
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def main():
    print("🚀 Setting up Website Uptime Monitor SaaS")
    print("=" * 50)
    
    # Check if virtual environment exists
    if not os.path.exists('.env'):
        print("\n📝 Creating .env file from template...")
        if os.path.exists('.env.example'):
            import shutil
            shutil.copy('.env.example', '.env')
            print("✅ .env file created. Please edit it with your configuration.")
        else:
            print("❌ .env.example not found")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing Python dependencies"):
        return False
    
    # Run migrations
    if not run_command("python manage.py makemigrations", "Creating database migrations"):
        return False
    
    if not run_command("python manage.py migrate", "Running database migrations"):
        return False
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput", "Collecting static files"):
        return False
    
    # Create superuser (optional)
    print("\n👤 Would you like to create a superuser account? (y/n): ", end="")
    if input().lower().startswith('y'):
        os.system("python manage.py createsuperuser")
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file with your configuration")
    print("2. Start Redis server: redis-server")
    print("3. Start Django: python manage.py runserver")
    print("4. Start Celery worker: celery -A uptime_monitor worker --loglevel=info")
    print("5. Start Celery beat: celery -A uptime_monitor beat --loglevel=info")
    print("\n🌐 Visit http://localhost:8000 to see your app!")

if __name__ == "__main__":
    main()