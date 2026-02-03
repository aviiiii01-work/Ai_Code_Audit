const { emailQueue } = require("../services/queueService");

exports.queueEmail = async (req, res) => {
  const { to, subject, body } = req.body;

  const job = await emailQueue.add({ to, subject, body });

  res.json({
    message: "Email queued successfully",
    jobId: job.id,
  });
};
