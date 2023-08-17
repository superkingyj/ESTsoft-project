// if ([] == false) {
//     console.log("true");
// } else {
//     console.log("false");
// }

// if ([[]] == false) {
//     console.log("true");
// } else {
//     console.log("false");
// }

// if (true + true + true == 3) {
//     console.log("true");
// } else {
//     console.log("false");
// }

// if (('b' + 'a' + + 'a' + 'a').toLowerCase == "banana") {
//     console.log("true");
// } else {
//     console.log("false");
// }

let a = '1' + 4;
let b = 4 - '1';
let c = 4 * '1';
let d = 4 / '1';
console.log(c);

// const examples = [
//     [0, ''],
//     [false, 'false'],
//     [null, undefined],
//     [NaN, NaN], // NaN: 숫자가 아닌 값. 자기 자신과도 같지 않음
//     [0, false],
//     [0, '\n'],
//     ['', '0'],
//     ['false', false],
//     [[], false],
//     [[], ''],
//     [[], 0],
//     [[0], false],
//     [[null], false],
//     [[undefined], false],
//     [{}, false],
//     [true, 1],
//     [true, '1'],
//     [true, [1]],
//     [true, { value: 1 }],
//     ['1', [1]],
//     [undefined, null],
//     [Infinity, Infinity],
//     [Infinity, 'Infinity'],
//     // [Symbol('foo'), Symbol('foo')],
//     [() => {}, () => {}]
// ];

// examples.forEach(([a, b]) => {
//     console.log(`${a} == ${b}: ${a == b}`);
//     console.log(`${a} === ${b}: ${a === b}`);
// });
