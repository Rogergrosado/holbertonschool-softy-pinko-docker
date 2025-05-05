# Use the latest version of Nginx as a parent image
FROM nginx:latest

# Copy the front-end files into the container at /var/www/html/softy-pinko-front-end
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copy the Nginx configuration file into the container at /etc/nginx/conf.d/default.conf
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

