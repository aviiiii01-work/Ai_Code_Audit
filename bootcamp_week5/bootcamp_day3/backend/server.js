const express = require("express");
const app = express();

const PORT = 3000;
const INSTANCE = process.env.INSTANCE_NAME || "unknown-instance";

app.get("/api", (req, res) => {
  res.json({ message: "Response from " + INSTANCE });
});

app.listen(PORT, () => console.log("Backend running:", INSTANCE));
