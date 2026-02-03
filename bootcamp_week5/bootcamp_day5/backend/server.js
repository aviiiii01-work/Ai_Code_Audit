const express = require("express");
const app = express();

const PORT = process.env.PORT || 3000;

app.get("/api", (req, res) => {
  res.json({ message: "Secure API Response" });
});

app.get("/health", (req, res) => {
  res.status(200).json({ status: "ok" });
});

app.listen(process.env.PORT, () => {
  console.log("Backend running on port", process.env.PORT);
});