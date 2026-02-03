# Week 5 Day 3 — NGINX Reverse Proxy + Load Balancing

## Overview
In this task, we create a scalable backend architecture with two backend instances and an NGINX reverse proxy inside Docker. All `/api` requests are routed to the backend replicas using round-robin load balancing.

## Folder Structure
bootcamp_week5/  
└── bootcamp_day3/  
 ├── backend/  
 │ ├── Dockerfile  
 │ └── server.js  
 ├── nginx/  
 │ ├── Dockerfile  
 │ └── nginx.conf  
 └── reverse-proxy-readme.md  

## Backend Setup
Dockerfile for backend:

FROM node:20  
WORKDIR /app  
COPY package.json .  
RUN npm install  
COPY . .  
EXPOSE 3000  
CMD ["npm", "start"]  


Server code (server.js):
const express = require("express");  
const app = express();  
const PORT = 3000;  
const INSTANCE = process.env.INSTANCE_NAME || "unknown-instance";  

app.get("/api", (req, res) => {  
 res.json({ message: "Response from " + INSTANCE });  
});  

app.listen(PORT, () => console.log("Backend running:", INSTANCE));  

Build & run backend containers:

docker build -t backend-service ./backend  
docker run -d --name backend1 -p 3001:3000 -e INSTANCE_NAME=backend-1 backend-service  
docker run -d --name backend2 -p 3002:3000 -e INSTANCE_NAME=backend-2 backend-service  

## NGINX Setup
NGINX configuration (nginx.conf):
events {}  
http {  
 upstream backend_cluster {  
  server backend1:3000;  
  server backend2:3000;  
 }  
 server {  
  listen 80;  
  location /api/ {  
   proxy_pass http://backend_cluster/;  
  }  
 }  
}  

NGINX Dockerfile:

FROM nginx:latest  
COPY nginx.conf /etc/nginx/nginx.conf  


Build & run NGINX container:

docker build -t my-nginx-proxy ./nginx  
docker run -d --name nginx-proxy -p 80:80 --link backend1 --link backend2 my-nginx-proxy  

## Test Load Balancing
Run multiple times:

curl http://localhost/api/  


Expected output alternates between backend-1 and backend-2:

{"message":"Response from backend-1"}  
{"message":"Response from backend-2"}  
{"message":"Response from backend-1"}  
{"message":"Response from backend-2"}  

## Final Outcome
- Two backend replicas running  
- One NGINX reverse proxy container  
- Automatic round-robin load balancing  
- Scalable multi-instance backend architecture
