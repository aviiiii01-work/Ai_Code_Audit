# Week 5 Day 4 — SSL + Self-Signed + mkcert + HTTPS

## Overview
In this task, we set up HTTPS for a Dockerized backend using NGINX as a reverse proxy. A self-signed certificate is generated with mkcert, and HTTP requests are redirected to HTTPS to ensure secure communication.

## Folder Structure
bootcamp_week5/  
└── bootcamp_day4/  
    ├── backend/  
    │   ├── Dockerfile  
    │   ├── package.json  
    │   └── server.js  
    ├── nginx/  
    │   ├── Dockerfile  
    │   ├── nginx.conf  
    │   └── certs/  
    │       ├── bootcamp.local.pem  
    │       └── bootcamp.local-key.pem  
    └── docker-compose.yml  

## Step 1 — Backend Setup
**backend/Dockerfile**  
FROM node:20  
WORKDIR /app  
COPY package.json .  
RUN npm install  
COPY . .  
EXPOSE 3000  
CMD ["node", "server.js"]  

**backend/server.js**  
const express = require("express");  
const app = express();  

app.get("/api", (req, res) => {  
  res.json({ message: "Secure API Response" });  
});  

app.listen(3000, () => console.log("Backend running on port 3000"));  

**backend/package.json**  
{  
  "name": "backend",  
  "version": "1.0.0",  
  "main": "server.js",  
  "dependencies": {  
    "express": "^4.18.2"  
  }  
}  

## Step 2 — Generate Self-Signed Certificate
Inside `bootcamp_day4/nginx` folder:  
mkcert bootcamp.local  
This generates `bootcamp.local.pem` and `bootcamp.local-key.pem` in the `certs/` folder.  

## Step 3 — NGINX Configuration
**nginx/Dockerfile**  
FROM nginx:latest  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY certs /etc/nginx/certs  

**nginx/nginx.conf**  
events {}  

http {  
  # Redirect ALL HTTP → HTTPS  
  server {  
    listen 80;  
    server_name bootcamp.local;  
    return 301 https://$host$request_uri;  
  }  

  # HTTPS server  
  server {  
    listen 443 ssl;  
    server_name bootcamp.local;  

    ssl_certificate     /etc/nginx/certs/bootcamp.local.pem;  
    ssl_certificate_key /etc/nginx/certs/bootcamp.local-key.pem;  

    location /api {  
      proxy_pass http://backend:3000;  
    }  
  }  
}  

## Step 4 — Docker Compose Setup
**docker-compose.yml**  
services:  
  backend:  
    build: ./backend  
    container_name: backend-secure  
    expose:  
      - "3000"  

  nginx:  
    build: ./nginx  
    container_name: nginx-secure  
    ports:  
      - "80:80"  
      - "443:443"  
    depends_on:  
      - backend  

## Step 5 — Run Containers
docker compose up -d --build  
Verify containers:  
docker ps  

## Step 6 — Test HTTPS
Open browser:  
https://bootcamp.local/api  
Expected response:  
{"message":"Secure API Response"}  

HTTP requests automatically redirect to HTTPS:  
curl http://bootcamp.local/api  # returns 301 Moved Permanently → HTTPS  

Command-line test:  
curl -k https://bootcamp.local/api  

## Final Outcome
- Backend container running on port 3000  
- NGINX container serving HTTPS on port 443  
- Self-signed certificate trusted by local system/browser  
- Automatic HTTP → HTTPS redirection  
- Secure API response verified  

This completes Week 5 Day 4 setup for SSL/TLS using self-signed certificates with mkcert.
