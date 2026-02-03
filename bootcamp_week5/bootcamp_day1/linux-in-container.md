# linux-in-container.md

## Linux Basics Inside a Docker Container — Week 5 Day 1
This document contains the observations and learnings while exploring Linux internals inside a Docker container running a Node.js application.

## 1. Entering the Docker Container
Command used: docker exec -it week5-container /bin/sh  
This opens an interactive shell inside the container.

## 2. Basic Linux Commands Checked
List files: ls , ls -la  
View running processes: ps , ps aux , top  
Check disk usage: df -h , du -sh .  
Check logs: ls /var/log , docker logs week5-container

## 3. Users & Permissions Inside Container
Current user: whoami  
View file permissions: ls -l  
Files copied during Docker build belong to root.

## 4. Filesystem Structure Verified
The container includes a minimal Linux filesystem: / , usr/ , bin/ , var/ , etc/ , tmp/ , app/ (working directory)

## 5. Observations About Docker Linux Environment
Containers are isolated Linux environments.  
PID 1 inside the container is the Node process (node app.js).  
Container has its own filesystem and OS packages.  
Stopping the container stops all processes inside it.  
Logs are viewed using Docker and not traditional Linux log files.

## 6. Useful Docker Commands Used
docker ps
docker logs week5-container
docker stop week5-container
docker start week5-container

## 7. Summary
By entering a Docker container and exploring Linux commands, we learned how processes, users, and filesystems work inside containers, how to inspect running apps and logs, and how Docker creates lightweight isolated OS environments. This completes the Week 5 Day 1 Linux-in-container exploration.
