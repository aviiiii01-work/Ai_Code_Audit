# Week 4 – Day 1 Backend Setup (Node.js + Express + Modular Architecture)

## 📌 Project Structure Overview
Your backend follows a clean, production-style structure:

src/
  ├── config/
  │     └── index.js
  ├── controllers/
  ├── jobs/
  ├── loaders/
  │     ├── app.js
  │     └── db.js
  ├── logs/
  │     └── app.log
  ├── middlewares/
  ├── models/
  ├── repositories/
  ├── routes/
  │     └── index.js
  ├── services/
  └── utils/
        └── logger.js

## 📌 Running the Project (Local Environment)
Use the following command:

NODE_ENV=local nodemon server.js

### Output Explanation
✔ Middlewares loaded  
✔ Routes mounted  
🚀 Server started on port 5000  
✔ Database connected  

### What this means:
- `.env.local` environment file is loaded successfully  
- Nodemon is active and watching file updates  
- `server.js` bootstraps the application  
- `app.js` loads all middlewares + routes  
- `db.js` creates a successful DB connection  
- Logs are written to `logs/app.log` using `logger.js`  

## 📌 Git Setup for Week 4 (Clean Initialization)
Initialize Git in the Week 4 folder:

cd ~/bootcamp/bootcamp_week4
git init
git add .
git commit -m "Initial commit for Week 4 Bootcamp tasks"

### Optional: Connect to GitHub
git branch -M main
git remote add origin <your_repo_url>
git push -u origin main

## ✔ Everything is correctly configured and running.
- Modular folder structure created  
- Server working  
- Database connected  
- Logger active  
- Ready to push to GitHub  
