# Use the latest Nginx image from Docker Hub
FROM nginx:latest

# Copy the custom Nginx configuration file to the container
COPY ./proxy.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for the proxy server
EXPOSE 80

