// 구구단.py

// 문제
// N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

// 입력
// 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

// 출력
// 출력형식과 같게 N*1부터 N*9까지 출력한다.

// 예제 입력 1
// 2

// 예제 출력 1
// 2 * 1 = 2
// 2 * 2 = 4
// 2 * 3 = 6
// 2 * 4 = 8
// 2 * 5 = 10
// 2 * 6 = 12
// 2 * 7 = 14
// 2 * 8 = 16
// 2 * 9 = 18


const fs = require('fs');
const path = require("node:path");
const filePath = process.platform === "linux" ? '/dev/stdin' : path.join(__dirname, 'input.txt');

let input = fs.readFileSync(filePath).toString().split("\n");
const n = input[0]

for (i = 1; i < 10; i++) {
    console.log(`${n} * ${i} = ${i * n}`);
}