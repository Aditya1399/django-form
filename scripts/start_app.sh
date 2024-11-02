set -e 
echo "Starting the application"

gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application --daemon

echo "Application started successfully"