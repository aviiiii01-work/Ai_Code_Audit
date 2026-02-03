const express = require("express");
const router = express.Router();
const { addEmailJob } = require("../services/queueService");

router.post("/send", async (req, res) => {
  const { to, subject, body } = req.body;
  try {
    await addEmailJob({ to, subject, body });
    res.status(200).json({ message: "Email job added to queue" });
  } catch (err) {
    res.status(500).json({ message: "Failed to add job", error: err.message });
  }
});

module.exports = router;
