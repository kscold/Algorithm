const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? '/dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);

let result = Array(n).fill(0);

for (let count = 1; count <= m; count++) {
    let [i, j, k] = input[count].split(' ').map(Number);

    for (let idx = i - 1; idx < j; idx++) {
        result[idx] = k;
    }
}

console.log(result.join(' '));