const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? 'dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim();

let result = [];
for (i = 97; i <= 122; i++) {
    result.push(input.indexOf(String.fromCharCode(i)));
}

console.log(result.join(' '));