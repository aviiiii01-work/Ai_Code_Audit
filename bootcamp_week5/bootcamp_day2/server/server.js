const express = require("express");
const mongoose = require("mongoose");

const app = express();

const mongoUrl = process.env.MONGO_URL || "mongodb://mongo:27017/mydb";

mongoose.connect(mongoUrl)
  .then(() => console.log("MongoDB connected"))
  .catch(err => console.error("DB Error:", err));

app.get("/", (req, res) => {
  res.json({ message: "Server running and connected to Mongo" });
});

app.listen(5000, () => console.log("Server running on port 5000"));
