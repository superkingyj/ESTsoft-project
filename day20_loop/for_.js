// javascript의 반복문
// for, of, in, foreach

// in - 인덱스에 접근
// const fruits = ["사과", "바나나", "수박"]
// for (const fruit in fruits){
//     console.log(fruit, typeof fruit, fruits[fruit])
// }
/**
출력
0 string 사과
1 string 바나나
2 string 수박
 */


// of - 요소 접근. (python의 in)
// const fruits = ["사과", "바나나", "수박"]
// for (const fruit of fruits){
//     console.log(fruit, typeof fruit, fruits[fruit])
// }
/*
사과 string undefined
바나나 string undefined
수박 string undefined
*/


// forEach
// 제어문 사용 불가 (break, continue)
// const fruits = ["사과", "바나나", "수박"]
// fruits.forEach((fruit, index) => {
//     console.log(fruit, typeof fruit, index)
// });


// map
// const numbers = [1,2,3,4,5];
// const square = numbers.map((numbers) => {
    //     return numbers**2;
    // });
    
// console.l~og(square);


// reduce
// const numbers = [1,2,3,4,5];
// const sum = numbers.reduce((accumulator, number) => {
//     return accumulator+number;
// }, 0);
// console.log(sum);


// filter
const number = [1,2,4,5,10];
const even = number.filter((number) => {
    if (number % 2 == 1){
        return true;
    }
    return false;

    // return number % 2 == 0;
});
console.log(even);