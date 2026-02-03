# Use official Node image
FROM node:18-alpine

# Set working directory inside container
WORKDIR /usr/src/app

# Copy package.json first (better for caching)
COPY package.json .

# Install dependencies
RUN npm install

# Copy all project files
COPY . .

# Expose the port your app uses
EXPOSE 3000

# Command to start the server
CMD ["npm", "start"]
