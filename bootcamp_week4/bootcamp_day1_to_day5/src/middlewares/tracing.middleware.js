const { v4: uuidv4 } = require("uuid");

function tracingMiddleware(req, res, next) {
  const requestId = req.headers["x-request-id"] || uuidv4();
  req.requestId = requestId;

  // Set the header so clients can see it
  res.setHeader("X-Request-ID", requestId);
  next();
}

module.exports = tracingMiddleware;
