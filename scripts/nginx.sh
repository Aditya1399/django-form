sudo systemctl daeomon-reload
sudo rm -f /etc/nginx/sites-enabled/default 

sudo cp /home/ubuntu/django/nginx/nginx.conf /etc/nginx/sites-available/myproject
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled/

sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx 
