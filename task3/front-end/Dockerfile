# Use the official Nginx image as a base image
FROM nginx:latest

# Copy the front-end files to Nginx server's HTML directory
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copy the Nginx configuration file to the container
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# Expose port 9000 to access the front-end
EXPOSE 9000

# Start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]

