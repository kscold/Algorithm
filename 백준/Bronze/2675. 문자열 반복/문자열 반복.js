const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? 'dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file).toString().trim().split('\n');

const t = parseInt(input[0]);

let result = '';
for (let i = 1; i <= t; i++) {
    let [r, s] = input[i].split(' ');
    r = parseInt(r);

    for (let j = 0; j < s.length; j++) {
        for (let k = 0; k < r; k++) {
            result += s[j];
        }
    }
    result += '\n';
}
console.log(result.trim());