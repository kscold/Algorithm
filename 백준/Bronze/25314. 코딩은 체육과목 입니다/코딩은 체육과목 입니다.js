const fs = require('fs');
const path = require('path');

const file = process.platform === 'linux' ? '/dev/stdin' : path.join(__dirname, 'input.txt');
const input = fs.readFileSync(file);

if (Number(input)) {
    let printLong = '';
    let count = Number(input) / 4;

    for (let i = 0; i < count; i++) {
        printLong += 'long ';
    }
    console.log(printLong + 'int');
}