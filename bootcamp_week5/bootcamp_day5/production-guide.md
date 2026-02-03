# 🚀 Bootcamp Week-5 — Full-Stack Docker Deployment Guide
## 1. Project Overview
This project demonstrates a **production-style full-stack architecture** using:
- **Frontend:** React + Vite  
- **Backend:** Node.js + Express  
- **Reverse Proxy:** Nginx  
- **Containerization:** Docker + Docker Compose  
- **Deployment Automation:** deploy.sh script  
- **Security:** HTTPS (SSL self-signed certificates for dev)  
- **CI-Style Practices:** Health checks, logging, restart policies, environment variables, profiles

## 2. Folder Structure
bootcamp_week5/bootcamp_day5/
├── 1. backend/
│   ├── server.js
│   ├── package.json
│   └── Dockerfile
├── 2. frontend/
│   ├── package.json
│   ├── vite.config.js
│   └── src/
├── 3. nginx/
│   ├── Dockerfile
│   ├── default.conf
│   └── certs/
├── 4. .env
├── 5. docker-compose.prod.yml
├── 6. deploy.sh
└── 7. production-guide.md


## 3. Environment Configuration
All sensitive data and configuration variables are stored in `.env` (never commit this file):
PORT=5000
NODE_ENV=production
JWT_SECRET=your_secret_key
The backend container reads these via `env_file` in `docker-compose.prod.yml`.

## 4. Docker Setup
### Backend Dockerfile
FROM node:20
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
EXPOSE 5000
CMD ["node", "server.js"]

### Frontend Dockerfile
FROM node:20
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
EXPOSE 5173
CMD ["npm", "run", "dev"]

### Nginx Dockerfile
FROM nginx:latest
COPY default.conf /etc/nginx/conf.d/default.conf
COPY certs /etc/nginx/certs

## 5. docker-compose.prod.yml
Key features implemented: Profiles for each service: `frontend`, `backend`, `nginx`;
Restart policy: `always`;
Healthchecks for containers: test: ["CMD", "curl", "-f", "http://localhost:5000/health"] interval: 10s timeout: 3s retries: 3;
Logging with rotation: driver: "json-file" options: max-size: "10m" max-file: "3";
Volumes: Persistent logs for Nginx;
Service dependency: Nginx waits for backend health check before starting.

## 6. Nginx Reverse Proxy Configuration
Routes `/api` → backend container; Serves frontend static files for all other routes;
 Redirects HTTP → HTTPS (dev certificates). Example default.conf: server { listen 80; location /api/ { proxy_pass http://backend_prod:5000/;
 proxy_set_header Host $host;
 proxy_set_header X-Real-IP $remote_addr; } location / { try_files $uri /index.html; } }

## 7. Deploying the Stack
Use deploy.sh for CI-style deployment: ./deploy.sh  
The script performs:
 1) Builds all services;
 2) Starts containers using `docker compose -f docker-compose.prod.yml up -d`;
 3) Shows logs for monitoring

## 8. Accessing the Application
Frontend: http://localhost (served by Nginx); Backend API: http://localhost/api; Health check: http://localhost/api/health  
⚠️ Do not use http://localhost:5173 for production — that is only the Vite dev server.

## 9. Monitoring & Maintenance
Check running containers: docker ps  
View container logs: docker logs backend_prod docker logs frontend_prod docker logs nginx_prod  
Stop all containers: docker compose -f docker-compose.prod.yml down

## 10. Key Best Practices Implemented
Environment variables stored in `.env`; Health checks ensure service availability; Automatic container restart policy; Log rotation for production stability; Docker profiles allow selective service deployment; CI-style deploy.sh ensures repeatable, safe deployment; Nginx reverse proxy + HTTPS for secure production setup

## ✅ Conclusion
Your Week-5 Day-5 project now represents a **fully production-ready containerized full-stack application**. It incorporates best practices of **Docker orchestration, service health, logging, environment security, and deployment automation**, and is ready for local or cloud deployment.
