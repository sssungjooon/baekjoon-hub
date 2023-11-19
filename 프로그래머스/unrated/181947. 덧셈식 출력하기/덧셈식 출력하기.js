const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    // console.log(Number(input[0]) + Number(input[1]));
    // console.log(input)
    const Num1 = Number(input[0])
    const Num2 = Number(input[1])
    console.log(`${Num1} + ${Num2} = ${Num1+Num2}`)
    
});