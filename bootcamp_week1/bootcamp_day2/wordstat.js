const fs = require("fs");
const { Worker } = require("worker_threads");
const { performance } = require("perf_hooks");

const args = process.argv;

// Read CLI arguments
const filePath = args[args.indexOf("--file") + 1];
const topCount = Number(args[args.indexOf("--top") + 1] || 10);
const minLen = Number(args[args.indexOf("--minLen") + 1] || 5);
const includeUnique = args.includes("--unique");
const concurrency = Number(args[args.indexOf("--conc") + 1] || 4);

if (!filePath) {
  console.log("Usage: node wordstat.js --file <filename> --top 10 --minLen 5 --unique");
  process.exit(1);
}

// function to run a worker on a given chunk
function runWorker(chunk, minLen) {
  return new Promise((resolve, reject) => {
    const worker = new Worker("./worker.js", { workerData: { chunk, min: minLen } });
    worker.on("message", resolve);
    worker.on("error", reject);
  });
}

async function main() {
  const start = performance.now();

  try {
    const fileData = await fs.promises.readFile(filePath, "utf8");

    // Split data into chunks depending on concurrency level
    const chunkSize = Math.ceil(fileData.length / concurrency);
    const chunks = [];
    for (let i = 0; i < concurrency; i++) {
      chunks.push(fileData.slice(i * chunkSize, (i + 1) * chunkSize));
    }

    // Process all chunks in parallel
    const processedResults = await Promise.all(chunks.map(c => runWorker(c, minLen)));

    // Merge all results
    let totalWords = 0;
    const freqMap = {};

    for (const part of processedResults) {
      totalWords += part.total;
      for (const [word, count] of Object.entries(part.freq)) {
        freqMap[word] = (freqMap[word] || 0) + count;
      }
    }

    const allWords = Object.keys(freqMap);
    const uniqueCount = allWords.length;
    const longestWord = allWords.reduce((a, b) => (b.length > a.length ? b : a), "");
    const topWords = Object.entries(freqMap)
      .sort((a, b) => b[1] - a[1])
      .slice(0, topCount);

    const result = {
      total: totalWords,
      longest: longestWord,
      top: topWords,
    };

    if (includeUnique) result.unique = uniqueCount;

    // save stats to file
    fs.writeFileSync("output/stats.json", JSON.stringify(result, null, 2));

    const end = performance.now();
    const runtime = (end - start).toFixed(2);

    const perf = { concurrency, time_ms: runtime };
    fs.writeFileSync("logs/perf-summary.json", JSON.stringify(perf, null, 2));

    console.log("✅ Analysis Complete!");
    console.log("📄 File:", filePath);
    console.log("🔹 Total Words:", totalWords);
    if (includeUnique) console.log("🔹 Unique Words:", uniqueCount);
    console.log("🔹 Longest Word:", longestWord);
    console.log("🔹 Top", topCount, "Words:", topWords.map(([w]) => w).join(", "));
    console.log("⚙️  Processed with", concurrency, "workers in", runtime, "ms");
  } catch (err) {
    console.error("❌ Error:", err.message);
  }
}

main();
