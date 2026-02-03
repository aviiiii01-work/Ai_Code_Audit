const express = require("express");
const dotenv = require("dotenv");
const tracingMiddleware = require("./src/middlewares/tracing.middleware");
const userRouter = require("./src/routes/user.routes");

dotenv.config();
require("./src/loaders/db");   

const app = express();

app.use(tracingMiddleware);
app.use(express.json());

// Routes
const emailRoutes = require("./src/routes/emailRoutes");
app.use("/api/email", emailRoutes);
app.use("/api/user", userRouter);

app.get("/", (req, res) => {
  res.status(200).json({
    success: true,
    message: "Server is running! Welcome to Bootcamp Week 4 Day 5 backend."
  });
});

app.use((req, res) => {
  res.status(404).json({
    success: false,
    message: "Route not found"
  });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () =>
  console.log(`Server running on http://localhost:${PORT}`)
);
