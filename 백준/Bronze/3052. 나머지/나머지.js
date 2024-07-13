const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? 'dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim().split('\n');

let result = 0;
const set = new Set();

for (i = 0; i < 10; i++) {
    const a = input[i];
    set.add(a % 42);
    result = [...set].length;
}

console.log(result);
