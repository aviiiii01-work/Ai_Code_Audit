const dotenv = require("dotenv");
const fs = require("fs");
const path = require("path");

module.exports = () => {
  const envFile = `.env.${process.env.NODE_ENV || "local"}`;

  dotenv.config({
    path: path.resolve(process.cwd(), envFile),
  });

  console.log(`Loaded environment: ${envFile}`);
};
