const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? '/dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim().split('\n');

const t = Number(input[0]);

let result = '';

for (let i = 1; i <= t; i++) {
    let num = input[i].split(' ');
    result += Number(num[0]) + Number(num[1]) + '\n';
}

console.log(result);