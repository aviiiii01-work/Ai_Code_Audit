const fs = require("fs");

const words = ["lorem", "ipsum", "dolar", "sit", "amet", "elit", "adipiscing", "curabitur"];
let data = [];
for (let i = 0; i < 200000; i++) {
    data.push(words[Math.floor(Math.random()*words.length)]);
}
fs.writeFileSync("corpus.txt", data.join(" "));
console.log("corpus.txt created")
