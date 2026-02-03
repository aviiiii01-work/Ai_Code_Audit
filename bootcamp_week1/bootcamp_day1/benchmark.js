const fs = require('fs')
const { performance } = require('perf_hooks')

function formatMemory(bytes) {
	return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
}

console.log('=== BUFFER TEST (fs.readfile) ===');
let start = performance.now();
let startMem = process.memoryUsage().rss;

fs.readFile('bigfile.txt', (err, data) => {
	if (err) throw err;
	let end = performance.now();
	let endMem = process.memoryUsage().rss;

	console.log(`Time Taken: ${(end - start).toFixed(2)} ms`);
	console.log(`Memory Used: ${formatMemory(endMem - startMem)}\n`);

	console.log('=== STREAM TEST (fs.createReadStream) ===');
	start = performance.now();
	startMem = process.memoryUsage().rss;

	const stream = fs.createReadStream('bigfile.txt');
	stream.on('data', chunk => {});
	stream.on('end', () => {
		end = performance.now();
		endMem = process.memoryUsage().rss;
		console.log(`Time Taken: ${(end - start).toFixed(2)} ms`);
		console.log(`Memory Used: ${formatMemory(endMem - startMem)}`);
	});
});

