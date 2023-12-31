/*
var: 함수 스코프 (한번 정의하면 함수 내에서 전부 다 사용 가능)
변수 호이스팅: 변수를 선언하기 이전에 참조하는 것
- 자바스크립트는 뒤에서 쭉 읽은 다음에 로드한 뒤에 실행시키기 때문에 호이스팅이 가능
- var만 가능
- 따라서 var이 아닌 let을 사용함
let: 블록 스코프 (한번 정의하면 블록 내에서만 사용 가능)
- 앞에서 정의가 되어야만 사용할 수 있음
*/

let x = 10; 

function example(){
    // var x; // 호이스팅 때문에 선언 안해도 실행됨
    let x = 10; 
    x = 20; 
    console.log(x);

    // 블록 스코프 시작
    if (true) {
        let x  = 20;
        console.log(x);
    }
    // 블록 스코프 끝
    
    console.log(x);
}
example();