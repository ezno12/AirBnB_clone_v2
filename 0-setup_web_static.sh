#!/usr/bin/env bash
# deployment of abnb web_static
rm /etc/nginx/sites-enabled/*~
apt-get update
apt-get install -y nginx
service nginx start

mkdir -p /data/web_static/releases /data/web_static/shared /data/web_static/releases/test
echo -e "<!DOCTYPE html>\n<html>\n    <head>\n    </head>\n    <body>\n        Holberton School\n    </body>\n</html>" | cat > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu  /data
sed -i '40i\        location /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
service nginx restart