// javascript의 함수 선언 방법 3가지

// 1.함수 선언
// 호이스팅 가능
let addNumber = add(3, 5);
console.log(addNumber);

function add(a,b){
    return a+b;
}


// 2. 함수 표현식
// 기본적으로 호이스팅 불가능
// 변수를 var로 선언하면 호이스팅 가능
const subtract1 = function(a,b){
    return a-b; 
};
console.log(subtract1(3, 5));


// 3. 화살표 함수
let subtract2 = (a, b) => {
    return  a-b;
};
console.log(subtract2(3, 5));