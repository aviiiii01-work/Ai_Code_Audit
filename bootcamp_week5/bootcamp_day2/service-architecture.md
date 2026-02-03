# Week 5 Day 2 — Multi-Container Architecture (Client + Server + Mongo)

- **Client (React)**
  - Runs dev server on port `5173`
  - Talks to API using `VITE_SERVER_URL` (e.g., `http://server:5000`)
  - Depends on backend API container

- **Server (Node + Express)**
  - Runs on port `5000`
  - Connects to MongoDB using `mongodb://mongo:27017/mydb`
  - Docker networking allows `mongo` hostname resolution

- **MongoDB**
  - Official `mongo:6` image
  - Data persisted using Docker volume: `mongo_data:/data/db`

- **Networking**
  - Docker Compose automatically creates a virtual network
    - Client → Server using hostname `server`
    - Server → Mongo using hostname `mongo`

- **Volumes**
  - MongoDB data persists even if container stops
  - Declared as: `volumes: - mongo_data:/data/db`

- **Commands**
  - Start complete system: `docker compose up -d`
  - View logs: `docker compose logs -f`
  - Stop everything: `docker compose down`

- **Notes**
  - Ensure Node.js version in Dockerfiles is 20+ for client (Vite) and server
  - Ports mapping:
    - Client: `5173:5173`
    - Server: `5000:5000`
    - Mongo: `27018:27017` (adjust if default port is busy)
  - Docker Compose automatically resolves container hostnames for inter-service communication
