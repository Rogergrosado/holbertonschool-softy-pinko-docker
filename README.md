# Softy Pinko Docker Project

## Project Overview

This project demonstrates the use of Docker to containerize an application that consists of multiple components: a front-end static content server, two API servers, a proxy server, and Docker Compose for managing all the containers. The application follows a multi-tier architecture where traffic is routed through a reverse proxy and load-balanced between API servers, all running inside Docker containers.

### High-Level Design

In this design, the architecture consists of a reverse proxy server, which routes requests to the appropriate back-end (API) or front-end (static content) server. The proxy also load balances API traffic between two servers using the Round Robin method.

**Round Robin Load Balancing:**  
Round Robin load balancing ensures an even distribution of requests across multiple servers. For example, if there are three servers A, B, and C, requests are sent sequentially to A, then B, then C, and the cycle repeats.

## Project Tasks

### 0. Create Your First Docker Image (Task 0)

- **Objective:** Create a Docker image based on the latest Ubuntu version, update the system, and display "Hello, World!" when the container runs.
- **Details:** A basic Dockerfile was created that sets up Ubuntu, updates the system, and runs a simple command to print "Hello, World!" in the terminal.
- **Outcome:** This task served as an introduction to Docker and the process of building and running containers.

### 1. Back-end Development (Task 1)

- **Objective:** Extend Task 0 by adding Python3, Flask, and setting up a basic Flask server with a single `/api/hello` endpoint returning "Hello, World!".
- **Details:** The Dockerfile was modified to install Python, Flask, and set up a Flask app. The app listens on port 5252 inside the container.
- **Outcome:** The Flask server was successfully set up and served the basic API response.

### 2. Front-end Development (Task 2)

- **Objective:** Create a front-end that communicates with the back-end.
- **Details:** The front-end was set up in a separate directory. An Nginx static file server was used to serve the front-end content. The back-end was reorganized into a `back-end` folder, and the front-end files were cloned from the [Softy Pinko Front-End](https://github.com/atlas-school/softy-pinko-front-end) repository.
- **Outcome:** The front-end was successfully integrated with the back-end API and served using Nginx.

### 3. Connecting Front-end and Back-end (Task 3)

- **Objective:** Enable dynamic data loading from the back-end to the front-end.
- **Details:** The front-end was updated with JavaScript to make AJAX requests to the back-end. Additionally, Flask-CORS was installed to allow cross-origin requests from the front-end to the back-end.
- **Outcome:** The front-end successfully communicated with the back-end, displaying dynamic data in response to user interactions.

### 4. Docker Compose (Task 4)

- **Objective:** Simplify the deployment using Docker Compose.
- **Details:** A `docker-compose.yml` file was created to manage the multi-container setup for the front-end, back-end, and proxy servers. Docker Compose allows us to spin up all services simultaneously.
- **Outcome:** Docker Compose streamlined the process of running the multi-container application with a single command.

### 5. Proxy Server (Task 5)

- **Objective:** Introduce a reverse proxy server to manage client requests.
- **Details:** Nginx was set up as a reverse proxy server to route traffic to either the front-end or back-end, depending on the URL path. The proxy server listens on port 80, and the front-end and back-end services no longer expose ports directly to the host machine.
- **Outcome:** The proxy server successfully routed requests, simplifying client-side interactions with the application.

### 6. Scaling Horizontally (Task 6)

- **Objective:** Scale the back-end horizontally by adding a second API server.
- **Details:** The `docker-compose.yml` file was updated to include two API servers. Nginx load-balances traffic between these two API servers using the Round Robin algorithm.
- **Outcome:** The application was able to handle increased traffic by distributing requests across two back-end servers, ensuring better performance and reliability.

## Docker Compose Configuration

The Docker Compose setup for this project uses multiple services:

- **front-end:** Serves static content using Nginx.
- **back-end:** Runs the Flask application, serving API endpoints.
- **proxy:** Acts as a reverse proxy and load balancer between the front-end and back-end servers.

### `docker-compose.yml` file structure:
```yaml
version: '3'
services:
  front-end:
    build: ./front-end
    ports:
      - "9000:9000"
  
  back-end:
    build: ./back-end
    ports:
      - "5252:5252"
  
  proxy:
    build: ./proxy
    ports:
      - "80:80"
    depends_on:
      - front-end
      - back-end

### Summary of Key Points
- **Tasks Overview:** The tasks progressively guide you through the steps of building the infrastructure for the application using Docker, including setting up the front-end, back-end, proxy server, load balancing, and scaling horizontally.
- **Docker Compose:** The `docker-compose.yml` file orchestrates the multi-container setup, ensuring everything runs together seamlessly.
- **Scaling:** Horizontal scaling was achieved by adding an additional API server and using Nginx as the load balancer.

