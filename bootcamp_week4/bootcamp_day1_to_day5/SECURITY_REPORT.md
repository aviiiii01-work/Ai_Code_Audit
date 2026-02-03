# SECURITY-REPORT.md

## Project: Bootcamp Week 4 - Day 1  
**Date:** 2025-12-01  
**Author:** Ravi Pratap Singh  

---

## 1. Introduction
This document summarizes the security measures applied and vulnerabilities tested in the Bootcamp Week 4 - Day 1 project. The focus is on common web application threats such as HTTP header attacks, NoSQL injection, XSS, rate limiting, and request validation. The project leverages **Express.js**, **MongoDB**, **Mongoose**, and **Joi** for robust API design.

---

## 2. Security Middleware Overview

| Middleware | Purpose |
|------------|---------|
| `helmet` | Secures HTTP headers (e.g., HSTS, X-Frame-Options, XSS protection) |
| `cors` | Controls Cross-Origin Resource Sharing policies |
| `express-rate-limit` | Limits repeated requests from the same IP |
| `xss-clean` | Sanitizes user input to prevent cross-site scripting attacks |
| `hpp` | Prevents HTTP parameter pollution |
| `mongoSanitizeFix` | Custom middleware to prevent NoSQL injection attacks |
| `express.json({ limit: "10kb" })` | Restricts payload size to prevent large payload attacks |

---

## 3. Validation & Data Integrity

- **Joi Schemas**:
  - `UserSchema`: Ensures `name`, `email`, `age`, and `role` follow proper types and constraints.
  - `ProductSchema`: Ensures `title`, `price`, `rating`, `status`, and `deletedAt` meet type and value constraints.
- **Purpose**:
  - Prevents invalid or malicious data from being stored in the database.
  - Provides clear error responses for invalid requests.
- **Integration with Mongoose**:
  - Joi validation is applied **before hitting Mongoose**, ensuring requests do not cause database-level errors.
  - Mongoose schema ensures additional layer of protection for required fields, types, defaults, and enums.

---

## 4. Vulnerabilities Tested & Results

| Vulnerability | Test Description | Result |
|---------------|-----------------|--------|
| **NoSQL Injection** | Attempted MongoDB operators in request body (e.g., `{ "$gt": "" }`) | Prevented by `mongoSanitizeFix`. All requests sanitized. ✅ |
| **Cross-Site Scripting (XSS)** | Submitted `<script>alert('xss')</script>` in input fields | Sanitized by `xss-clean`. Payload neutralized. ✅ |
| **HTTP Parameter Pollution (HPP)** | Sent duplicate query parameters (e.g., `?id=1&id=2`) | Prevented by `hpp` middleware. Only the first value considered. ✅ |
| **Rate Limiting** | Exceeded 100 requests per 15 minutes from same IP | Blocked with message: "Too many requests from this IP, please try again later". ✅ |
| **Invalid Input / Missing Fields** | Sent incomplete payloads for User/Product creation | Rejected with clear Joi validation errors. ✅ |
| **Invalid Enum / Type** | Submitted invalid `status` or `role` | Rejected via Joi or Mongoose validation. ✅ |
| **Large Payloads** | Sent request body >10KB | Rejected by `express.json({ limit: "10kb" })`. ✅ |
| **HTTP Header Attacks** | Checked for missing security headers | Secured by `helmet`. Headers like HSTS, X-Frame-Options present. ✅ |
| **Soft Delete / Data Integrity** | Deleted Product using API | `deletedAt` populated, data integrity maintained. ✅ |

---

## 5. Notes / Recommendations

1. **Environment Variables**
   - Loaded via `dotenv` and `.env.local`. Sensitive keys not hardcoded.
2. **Logging**
   - `logger.js` available for tracking suspicious activities.
3. **Future Improvements**
   - Add authentication & authorization for sensitive routes.
   - Implement HTTPS in production.
   - Use content security policy (CSP) headers for stronger XSS protection.

---

## 6. Conclusion

The application has been tested against common security vulnerabilities. The applied middleware, along with input validation and soft delete practices, ensures that the system is resistant to NoSQL injection, XSS, HPP, rate-limit abuse, and other basic attacks.  

All tested cases passed successfully. The system is **secure for development and testing purposes**.
