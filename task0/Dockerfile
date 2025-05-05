# Use the latest version of Ubuntu as a parent image
FROM ubuntu:latest

# Update the package lists for upgrades for packages that need upgrading
RUN apt-get update

# Upgrade all the installed packages
RUN apt-get upgrade -y

# When the Docker container is run, echo "Hello, World!"
CMD echo "Hello, World!"
