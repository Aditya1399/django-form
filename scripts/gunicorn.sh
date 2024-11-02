sudo cp /home/ubuntu/django/gunicorn/gunicorn.socket /etc/systemd/system/gunicorn.socket 
sudo cp /home/ubuntu/django/gunicorn/gunicorn.services /etc/systemd/system/gunicorn.service

sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service

