set -e 
echo "Stopping the application"
pkill -f "gunicorn"
echo "Application stopped successfully"
