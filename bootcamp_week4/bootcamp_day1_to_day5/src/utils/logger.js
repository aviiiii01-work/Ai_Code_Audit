const { createLogger, transports, format } = require("winston");

const logger = createLogger({
  level: "info",
  format: format.combine(
    format.timestamp(),
    format.json()
  ),
  transports: [
    new transports.Console(),
    new transports.File({ filename: "src/logs/app.log" }),
  ],
});

function info(message, meta = {}) {
  const logMsg = meta.requestId ? `[${meta.requestId}] ${message}` : message;
  console.log(logMsg, meta);
}

function error(message, meta = {}) {
  const logMsg = meta.requestId ? `[${meta.requestId}] ${message}` : message;
  console.error(logMsg, meta);
}

module.exports = { info, error ,logger};
