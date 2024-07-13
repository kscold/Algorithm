const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? '/dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim();

const n = Number(input);

const memo = Array(n + 1).fill(0);
memo[1] = 1;
memo[2] = 1;

for (i = 3; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2];
}

console.log(memo[n]);