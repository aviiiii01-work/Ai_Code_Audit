const express = require("express");
const app = express();
const productRoutes = require("../routes/product.routes");
const userRoutes = require("../routes/user.routes");
const securityMiddleware = require("../middlewares/security");

securityMiddleware(app);

app.use("/api/products", productRoutes);
app.use("/api/users", userRoutes);

// Optional: catch-all 404 handler
app.use((req, res, next) => {
  res.status(404).json({ success: false, message: "Route not found" });
});
  
module.exports = app;
