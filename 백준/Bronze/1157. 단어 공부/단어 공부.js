const fs = require('fs');
const path = require('path');
const file = process.platform === 'linux' ? 'dev/stdin' : path.join(__dirname, 'input.txt');

const input = fs.readFileSync(file).toString().trim().split('\n');

const word = input[0].toLowerCase();

const obj = {};

for (let i = 0; i < word.length; i++) {
    if (obj[word[i]] === undefined) {
        obj[word[i]] = 1;
    } else {
        obj[word[i]] += 1;
    }
}

let result = '';
let count = 0;

for (key in obj) {
    if (obj[key] > count) {
        count = obj[key];
        result = key.toUpperCase();
    } else if (obj[key] === count) {
        result = '?';
    }
}

console.log(result);
