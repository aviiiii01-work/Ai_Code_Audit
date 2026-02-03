const { Worker } = require('bullmq');
const IORedis = require('ioredis');
const { info, error } = require('../utils/logger');

const connection = new IORedis({
  host: process.env.REDIS_HOST || "127.0.0.1",
  port: process.env.REDIS_PORT || 6379
});

const worker = new Worker(
  "email-queue",
  async (job) => {
    info("processing_job", { jobId: job.id, data: job.data });

    await new Promise((r) => setTimeout(r, 1000)); // simulate email send

    return { status: "Email sent" };
  },
  { connection }
);

worker.on("failed", (job, err) => {
  error("worker_failed", { jobId: job.id, error: err.message });
});

module.exports = worker;
