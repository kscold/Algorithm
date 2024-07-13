const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? 'dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);

let bastkets = Array(n).fill(0);
bastkets.map((bastket, i) => (bastkets[i] = i + 1));

for (let i = 1; i <= m; i++) {
    const [a, b] = input[i].split(' ').map(Number);

    let temp = [];

    for (let j = a - 1; j < b; j++) {
        temp.push(bastkets[j]);
    }
    temp.reverse();
    bastkets.splice(a - 1, b - a + 1, ...temp);
}

console.log(bastkets.join(' '));
