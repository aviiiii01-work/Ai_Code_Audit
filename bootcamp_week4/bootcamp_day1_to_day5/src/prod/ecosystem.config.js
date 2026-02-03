module.exports = {
  apps: [
    {
      name: "bootcamp-api",
      script: "src/server.js",
      instances: 1,
      autorestart: true 
    }
  ]
};
