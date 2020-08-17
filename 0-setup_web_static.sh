#!/usr/bin/env bash
# Prepare your web servers
apt -y update
apt install -y nginx
sed -i '/server_name _/a location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwlsu4? permanent; }' /etc/nginx/sites-available/default
sed -i "/server_name _/ a\\\tadd_header X-Served-By \"\$HOSTNAME\";" /etc/nginx/sites-available/default
sed -i '/server_name _/a error_page 404 /404.html; location = /404.html {root /var/www/html/; internal; }' /etc/nginx/sites-available/default
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart
exit 0
