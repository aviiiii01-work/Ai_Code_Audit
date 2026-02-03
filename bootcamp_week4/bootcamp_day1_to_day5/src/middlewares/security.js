// src/middlewares/security.js

const helmet = require("helmet");
const cors = require("cors");
const rateLimit = require("express-rate-limit");
const hpp = require("hpp");
const express = require("express"); // for body parser
const { escape } = require("validator"); // npm install validator

// Custom NoSQL Injection sanitizer
const sanitize = (obj) => {
  if (!obj) return obj;
  for (let key in obj) {
    if (typeof obj[key] === "object") sanitize(obj[key]);
    if (key.startsWith("$") || key.includes(".")) {
      const safeKey = key.replace(/\$/g, "_").replace(/\./g, "_");
      obj[safeKey] = obj[key];
      delete obj[key];
    }
  }
  return obj;
};

const mongoSanitizeFix = (req, res, next) => {
  req.body = sanitize(req.body);
  req.params = sanitize(req.params);
  next();
};

// Custom XSS sanitizer
const xssSanitizeFix = (req, res, next) => {
  const sanitizeStrings = (obj) => {
    if (!obj) return obj;
    for (let key in obj) {
      if (typeof obj[key] === "object") sanitizeStrings(obj[key]);
      else if (typeof obj[key] === "string") obj[key] = escape(obj[key]);
    }
    return obj;
  };
  req.body = sanitizeStrings(req.body);
  req.params = sanitizeStrings(req.params);
  next();
};

const securityMiddleware = (app) => {
  // 1️⃣ Secure HTTP headers
  app.use(helmet());

  // 2️⃣ Enable CORS
  app.use(cors());

  // 3️⃣ Rate limiting
  const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100,
    message: { success: false, message: "Too many requests from this IP, try later" },
  });
  app.use(limiter);

  // 4️⃣ Prevent HTTP Parameter Pollution
  app.use(hpp());

  // 5️⃣ Body parser size limit
  app.use(express.json({ limit: "10kb" }));

  // 6️⃣ Apply Node 24-safe sanitizers
  app.use(mongoSanitizeFix);
  app.use(xssSanitizeFix);
};

module.exports = securityMiddleware;
