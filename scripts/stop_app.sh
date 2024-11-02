set -e 
echo "Stopping the application"
pskill -f "gunicorn"
echo "Application stopped successfully"
