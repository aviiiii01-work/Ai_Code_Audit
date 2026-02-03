# 🚀 Deployment Notes - Bootcamp Week 4 Day 5 Backend

This document explains deployment steps for the backend project using Express, MongoDB, Redis, and BullMQ workers.

## 1. Project Structure
project/
│── server.js
│── .env
│── src/
│   ├── routes/
│   ├── controllers/
│   ├── models/
│   ├── jobs/
│   │    ├── queues/
│   │    └── workers/
│   ├── loaders/
│   └── middlewares/

## 2. Environment Variables
Create `.env` in project root:
MONGO_URI=mongodb://127.0.0.1:27017/bootcamp_day1
PORT=5000
REDIS_HOST=127.0.0.1
REDIS_PORT=6379

## 3. MongoDB Setup
Check Mongo service: `sudo systemctl status mongod`  
Start MongoDB: `sudo systemctl start mongod`

## 4. Redis Setup
Install Redis (Ubuntu): `sudo apt install redis-server`  
Enable & Start Redis: `sudo systemctl enable redis-server && sudo systemctl start redis-server`  
Test: `redis-cli ping` → should return `PONG`

## 5. Install Dependencies
Run: `npm install`  
Key packages: express, mongoose, bullmq, ioredis, dotenv, nodemon (dev)

## 6. Start Server
Development: `nodemon server.js`  
Production: `npm start`  
API URL: `http://localhost:5000`

## 7. Run Worker
Worker must run separately: `node src/jobs/workers/email.worker.js`  
Expected output: `Processing email job... Job completed`

## 8. Testing Email Queue (Postman)
POST `http://localhost:5000/api/email/send`  
Body (JSON):
{
  "to": "test@example.com",
  "subject": "Hello from Queue",
  "body": "This is a test email job"
}  
Response: `{ "message": "Email job added to queue" }`  
Worker Output: `Processing email job... Job completed`

## 9. Root Route Health Check
GET `http://localhost:5000/` → Expected:
{
  "success": true,
  "message": "Server is running! Welcome to Bootcamp Week 4 Day 5 backend."
}

## 10. Reverse Proxy (Production)
NGINX example:
server {
    listen 80;
    server_name your_domain.com;
    location / {
        proxy_pass http://localhost:5000;
    }
}
Restart NGINX: `sudo systemctl restart nginx`

## 11. Important Notes
- API server & Worker must run separately  
- Redis must be running before Worker  
- `MONGO_URI` must be correct  
- Do not commit `.env`  

🎉 Deployment complete! Backend is ready with Express + MongoDB + Redis + BullMQ.
