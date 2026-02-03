const { Queue } = require("bullmq");
const redis = require("../../db/redis");

const emailQueue = new Queue("email-queue", {
  connection: redis,
});

async function addEmailJob(data) {
  await emailQueue.add("send-email", data, {
    attempts: 3,
    backoff: {
      type: "exponential",
      delay: 2000,
    },
    removeOnComplete: true,
    removeOnFail: false,
  });
}

module.exports = { emailQueue, addEmailJob };
