const { Worker } = require("bullmq");

const connection = {
  host: "127.0.0.1",
  port: 6379,
  maxRetriesPerRequest: null,
};

const worker = new Worker(
  "email-queue",
  async (job) => {
    console.log("Processing email job...", job.data);
  },
  { connection }
);

worker.on("completed", (job) => {
  console.log(`Job ${job.id} completed`);
});

worker.on("failed", (job, err) => {
  console.log(`Job ${job.id} failed: ${err.message}`);
});
