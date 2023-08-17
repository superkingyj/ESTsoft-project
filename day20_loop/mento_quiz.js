// 1.JavaScript를 사용하여 아래의 작업을 완료하세요

// 1.div 요소를 선택하고 변수 container 에 할당하세요
const container1 = document.getElementById("container");
console.log(container1);


// 2. Hello, world에 클래스('boldText')를 추가하세요
const h1 = document.querySelector('a');
h1.classList.add("boldText");
console.log(h1);


// 3. forEach 메서드를 이용해 Item 1, 2, 3의 텍스트 컬러를 파랑색으로 바꾸세요
const items1 = document.getElementsByTagName('li');
for (let item of items1){
    item.style.color = 'blue';
}
console.log(document.getElementsByTagName('li'));

// 4. class가 "description"인 모든 요소를 한번에 선택하고 클릭시에 알림창이 뜨도록 바꾸세요
function alertFunc(){
    console.log("눌림");
    alert("alert 테스트");
}

const buttons = document.querySelectorAll(".alert");
console.log(buttons);
buttons.forEach(button => {
    button.addEventListener("click", alertFunc);
})

// 5.'This is a nother paragraph.'를 '이것은 문장입니다'로 바꾸세요
const descriptions2 = document.getElementsByClassName("description");
descriptions2[1].textContent = "이것은 문장입니다.";


// 6. div 내에 <h2>Bye, world!</h2>를 추가하세요
const container2 = document.getElementsByTagName("div")[0];
let newH2 = document.createElement('h2');
newH2.textContent="Bye, world!";
container2.appendChild(newH2);


// 7. Item 2 요소를 제거하세요
const items2 = document.getElementsByTagName('li');
items2[1].remove();



// 2. 클릭을 3번했을때 사라지는 버튼을 만드세요
const button = document.getElementById('btn');
let cnt = 0;
button.onclick = function(){
    cnt += 1;
    if (cnt === 3){
        button.remove();
    }
}