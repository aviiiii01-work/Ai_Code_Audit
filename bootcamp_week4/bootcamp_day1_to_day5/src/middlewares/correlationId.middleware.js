const { v4: uuid } = require("uuid");

function correlationId(req, res, next) {
  const id = req.headers["x-request-id"] || uuid();
  req.requestId = id;
  res.setHeader("X-Request-ID", id);
  next();
}

module.exports = correlationId;
