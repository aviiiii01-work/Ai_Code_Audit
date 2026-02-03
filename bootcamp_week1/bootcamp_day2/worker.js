const { parentPort, workerData } = require("worker_threads");

function analyzeChunk(text, minLen) {
  const words = text.match(/\b[a-zA-Z]+\b/g) || [];
  const filtered = words.filter(w => w.length >= minLen);
  const map = {};

  for (const word of filtered) {
    map[word] = (map[word] || 0) + 1;
  }

  return { total: filtered.length, freq: map };
}

const output = analyzeChunk(workerData.chunk, workerData.min);
parentPort.postMessage(output);
