// server.js
const http = require("http");
const { URL } = require("url");

const PORT = process.env.PORT || 3000;

// Common response helper
function sendJSON(res, status, data, headers = {}) {
  res.writeHead(status, { "Content-Type": "application/json", ...headers });
  res.end(JSON.stringify(data, null, 2));
}

const server = http.createServer((req, res) => {
  const urlObj = new URL(req.url, `http://${req.headers.host}`);
  const path = urlObj.pathname;
  const method = req.method;

  // Log each request neatly
  console.log(`[${new Date().toISOString()}] ${method} ${path}`);
  // Home Page: Welcomes! you  
  if (path === "/") {
    return sendJSON(res, 200, { message: "Welcome to my server!" });
    }

  // Endpoint 1: /echo → Return request headers
  if (path === "/echo") {
    return sendJSON(res, 200, {
      message: "Echoing your request headers",
      headers: req.headers,
    });
  }

  // Endpoint 2: /slow?ms=3000 → Delay response
  if (path === "/slow") {
    const delay = Math.min(parseInt(urlObj.searchParams.get("ms")) || 1000, 10000); // cap at 10s
    return setTimeout(
      () => sendJSON(res, 200, { message: `Responded after ${delay} ms delay` }),
      delay
    );
  }

  // Endpoint 3: /cache → Demonstrate ETag and caching
  if (path === "/cache") {
    const ETag = '"demo-xyz-123"';
    if (req.headers["if-none-match"] === ETag) {
      res.writeHead(304, { "Cache-Control": "max-age=60", ETag });
      return res.end(); // 304 Not Modified
    }
    return sendJSON(
      res,
      200,
      { message: "Fresh response from /cache endpoint" },
      { "Cache-Control": "max-age=60", ETag }
    );
  }
  // Endpoint: /time → Return current server time

  // Endpoint: /time → Return current server time (ISO + human-readable)
    if (path === "/time") {
        const now = new Date();
        const humanReadable = now.toLocaleString(); // e.g., "11/7/2025, 5:30:12 PM"
        return sendJSON(res, 200, {
            iso: now.toISOString(),
            local: humanReadable
        });
    }

  // Default route → 404
  sendJSON(res, 404, { error: "Not Found", path });
});

server.listen(PORT, () => {
  console.log(`🚀 Server is running at http://localhost:${PORT}`);
});
