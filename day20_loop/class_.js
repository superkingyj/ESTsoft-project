// 클래스는 코드의 앞에 적어주는 것이 좋음

// ES5 버전 클래스
// fucntion 선언문을 사용하기 때문에 호이스팅 되지만 안하는걸 권장
// function Person(name, age) {
//     this.name = name;
//     this.age = age;
//     this.sayHello = function(){
//         console.log(`안녕하세요, 제 이름은 ${name}, 나이는 ${age}입니다.`)
//     };
// }


// ES6버전 클래스
// class로 선언함
// constructor 있음
// 호이스팅 안됨
// class Person{
//     constructor(name, age){
//         this.name = name;
//         this.age = age;
//     }
//     sayHello() {
//         console.log(`안녕하세요! 제 이름은 ${this.name}, 그리고 나이는 ${this.age}입니다.`)
//     }
// }

// let Human = new Person("김유진", 20);
// Human.sayHello();


// 클래스 표현식
// 호이스팅 안됨
let rectangle = class {
    constructor(height, width){
        this.height = height;
        this.width = width;
        
    }

    calcArea(){
        return this.height * this.width;
    }
};

const square = new rectangle(5, 9);
console.log(square.calcArea());