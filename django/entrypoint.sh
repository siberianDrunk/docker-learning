#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
gunicorn --bind 0.0.0.0:8005 deep_sfu.wsgi:application
