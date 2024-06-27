const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? '/dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);

let baskets = Array(n).fill(0);
baskets = baskets.map((basket, i) => (baskets[i] = i + 1));

for (i = 1; i <= m; i++) {
    const [I, J] = input[i].split(' ').map(Number);

    let tmpIndex = baskets[I - 1];

    baskets[I - 1] = baskets[J - 1];
    baskets[J - 1] = tmpIndex;
}
console.log(baskets.join(' '));