# API Investigation - Day 4

## Overview
This document provides an investigation of the Node.js HTTP server built in Day 4. It includes details of all implemented endpoints, their behavior, testing methodology using `curl`, and observations regarding server responses.

## Server Setup
- **File:** `server.js`
- **Port:** `3000` (default)  
- **Server Module:** `http` (built-in Node.js module)  
- **Purpose:** To demonstrate basic REST API concepts including routing, query parameters, delays, and caching.

### Server Start
```bash
node server.js
```
**Output:**
```
🚀 Server is running at http://localhost:3000
```

### Server Stop
- Press `Ctrl + C` in the terminal to stop the server.

## Endpoints Implemented

### 1. `/echo`
- **Method:** GET
- **Description:** Returns all request headers in JSON format.
- **Usage Example:**
```bash
curl http://localhost:3000/echo
```
- **Sample Output:**
```json
{
  "message": "Echoing your request headers",
  "headers": {
    "host": "localhost:3000",
    "user-agent": "curl/8.5.0",
    "accept": "*/*"
  }
}
```

### 2. `/slow`
- **Method:** GET
- **Query Parameter:** `ms` (optional, delay in milliseconds)
- **Description:** Delays response by a specified number of milliseconds. Max delay capped at 10 seconds.
- **Usage Example:**
```bash
curl "http://localhost:3000/slow?ms=3000"
```
- **Sample Output:**
```json
{
  "message": "Responded after 3000 ms delay"
}
```

### 3. `/cache`
- **Method:** GET
- **Headers:** Supports `If-None-Match` for ETag-based caching
- **Description:** Demonstrates caching behavior. Returns `304 Not Modified` if client sends matching ETag.
- **Usage Examples:**
```bash
curl -i http://localhost:3000/cache
curl -i -H 'If-None-Match: "demo-xyz-123"' http://localhost:3000/cache
```
- **Sample Output (200 OK):**
```json
{
  "message": "Fresh response from /cache endpoint"
}
```
- **Sample Output (304 Not Modified):**
```
HTTP/1.1 304 Not Modified
Cache-Control: max-age=60
ETag: "demo-xyz-123"
```

### 4. Default Route
- **Path:** Any undefined route (e.g., `/`, `/greet`, `/time` if not implemented)
- **Response:** 404 Not Found
- **Sample Output:**
```json
{
  "error": "Not Found",
  "path": "/"
}
```

## Testing Methodology

1. **Using curl:**
   - Test endpoint responses in terminal.
   - Validate headers, query parameters, caching behavior, and delays.
   - Examples:
```bash
curl http://localhost:3000/echo
curl "http://localhost:3000/slow?ms=2000"
curl -i http://localhost:3000/cache
curl -i -H 'If-None-Match: "demo-xyz-123"' http://localhost:3000/cache
```

2. **Using browser:**
   - Opening `http://localhost:3000/` shows 404 JSON because no route `/` is defined.
   - Correct endpoints must be appended to the URL (e.g., `/echo`, `/slow`, `/cache`).

3. **Observations from Tests:**
   - Delayed responses work as expected.
   - ETag caching responds with `304` when header matches.
   - Undefined routes consistently return structured JSON error.

## Lessons Learned

- Node.js `http` module allows basic server creation without frameworks.
- URL parsing using `URL` class makes query parameter extraction straightforward.
- JSON responses can be standardized with helper functions.
- ETag headers are a simple mechanism to demonstrate caching behavior.
- Testing APIs in terminal with `curl` provides immediate feedback.
- Browser testing may show 404 for undefined paths; always use correct endpoints.

## Next Steps / Recommendations

1. Implement additional endpoints:
   - `/greet?name=<your_name>` → Responds with personalized greeting
   - `/time` → Returns current server time
2. Improve `/cache` to support dynamic content with unique ETags.
3. Explore `express.js` for cleaner routing and middleware support.
4. Document all endpoints with a tool like Swagger for future scalability.
