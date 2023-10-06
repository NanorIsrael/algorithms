#!/usr/bin/env bash
# Install nginx on your web-01 server

# sudo apt-get -y update
# sudo apt-get -y install nginx
# sudo service nginx start

#ufw allow 'Nginx HTTP'

# Get the hostname of the server
HOSTNAME=$(hostname)

# Define the Nginx configuration file path
NGINX_CONF_PATH="/etc/nginx/sites-available/default"

sudo chown -R $USER:$USER "/etc/nginx"
sudo chown -R $USER:$USER "/var/www"
sudo chown -R $USER:$USER "/usr/share/nginx/html"

STRING="Hello World!"

folder_name="/data"

if [ ! -d "$folder_name" ]; then
	sudo mkdir "$folder_name"
fi
# mkdir "/data/web_static/"
# mkdir "/data/web_static/"
# mkdir "/data/web_static/releases/ "=
# mkdir "/data/web_static/shared/"
# mkdir "/data/web_static/releases/test/"

# echo "$STRING" > "/data/web_static/releases/test/index.html"

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
# "/data/web_static/current"






REDIRECT="\n\tlocation /redirect_me {\n\t\treturn 301 http://dev-israel.tech;\n\t\tadd_header X-Served-By $HOSTNAME;\n\t}\n"
FILE="/etc/nginx/sites-available/default"

ERRORFILE="/usr/share/nginx/html/404error.html"
FOUR="Ceci n'est pas une page"
ERRORREDIRECT="\n\terror_page 404 /404error.html;\n\tlocation = /404error.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t\tadd_header X-Served-By $HOSTNAME;\n\t}\n"

sed -i "37i\ $REDIRECT" "$FILE"
echo "$FOUR" > "$ERRORFILE"
sed -i "37i\ $ERRORREDIRECT" "$FILE"

sudo sed -i "33i\ \n\t\tadd_header X-Served-By $HOSTNAME;\n\t" "$FILE"

sudo service nginx restart