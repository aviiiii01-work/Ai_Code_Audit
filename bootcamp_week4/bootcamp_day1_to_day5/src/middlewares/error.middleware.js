module.exports = (err, req, res, next) => {
  const code = err.statusCode || 400;

  res.status(code).json({
    success: false,
    message: err.message || "Something went wrong",
    code,
    timestamp: new Date(),
    path: req.originalUrl
  });
};
