# Use the latest version of Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package lists and install required dependencies in one step
RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment in /env
RUN python3 -m venv /env

# Set the virtual environment's bin directory to the PATH so we use pip from the virtual environment
ENV PATH="/env/bin:$PATH"

# Install Flask and Flask-CORS using pip within the virtual environment
RUN pip install flask flask-cors

# Set the working directory to /app
WORKDIR /app

# Copy only the necessary files for the backend to the container
COPY ./api.py /app/api.py

# Expose the port for the backend
EXPOSE 5252

# Run api.py when the container launches
CMD ["python", "api.py"]

