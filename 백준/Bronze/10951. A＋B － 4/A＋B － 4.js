const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? '/dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim().split('\n');

for (let i = 0; i < input.length; i++) {
    let result = input[i].split(' ');

    console.log(Number(result[0]) + Number(result[1]));
}