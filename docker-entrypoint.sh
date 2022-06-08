#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

# Collect all static files
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
gunicorn config.wsgi:application --bind 0.0.0.0:8000
