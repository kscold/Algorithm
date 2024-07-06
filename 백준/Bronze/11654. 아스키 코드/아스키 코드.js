const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? 'dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim();

const ascii = input.charCodeAt(0);

console.log(ascii);