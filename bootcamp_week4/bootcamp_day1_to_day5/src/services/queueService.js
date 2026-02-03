const { Queue } = require("bullmq");

const connection = {
  host: "127.0.0.1",
  port: 6379,
  maxRetriesPerRequest: null,
};

const emailQueue = new Queue("email-queue", {
  connection,
});

async function addEmailJob(data) {
  await emailQueue.add("send-email", data, {
    attempts: 3,
    backoff: {
      type: "exponential",
      delay: 3000,
    },
  });
}

module.exports = {
  emailQueue,
  addEmailJob,
};
