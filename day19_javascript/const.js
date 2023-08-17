/*
const: 바뀌지 않는 고정된 값을 쓸 때 사용함
- ex) 원주율

*/
const PI = 3.141592;
console.log(PI);

// PI = 3.14; // 에러 
// console.log(PI);


const person = {
    name: "John",
    age: 20
};

person.age = 21;
person.name = "김유진";
console.log(person);