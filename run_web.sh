#!/bin/bash

cd backend

echo Migrations
python manage.py migrate                  # Apply database migrations

# echo Static files
python manage.py collectstatic --noinput  # Collect static files

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn backend.wsgi:application --bind 0.0.0.0:8080 --workers=5 --threads=2 --worker-class=gthread --timeout 600 --graceful-timeout 600
