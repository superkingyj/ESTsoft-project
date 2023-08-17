// HTML 요소 가져ㅇㅎ가

// 1.ID로 가져오는 방법
const elementById = document.getElementById('section1');
console.log(elementById);

// // 2.클래스로 가져오는 방법
const elementByClass = document.getElementsByClassName("mySection");
console.log(elementByClass);

// // 3.태그명으로 가져오는 방법
const elementByTagName = document.getElementsByTagName("section");
console.log(elementByTagName);

// 4. 각각의 요소를 가져오는 방법
// 제일 많이 씀
// 참고 - day13_crawling/naver_news.py
const elementBySelector = document.querySelector("#section2 > h2");
console.log(elementBySelector);



// 스타일 변경 (css로 스타일을 입히는게 더 효율적임)

// 1. 스타일 각각 설정
const section2header = document.querySelector("#section2 > h2");
section2header.style.color = 'red';

const section1header = document.getElementById("section1").getElementsByTagName('h2')[0]; // Tag로 가져오면 컬렉션 값으로 가져오므로 [0]으로 접근
section1header.style.color = 'red';

// 2. 스타일 한번에 설정
const sectionHeaders = document.getElementsByClassName("mySection");

for (let section of sectionHeaders){
    let h2 = section.getElementsByTagName('h2')[0];
    h2.style.color = 'red';
    h2.style.fontSize = '30px';
}


// 버튼 동작시키기
const button = document.getElementById('btn');
button.addEventListener("click", handleClick);

const buttonContainer = document.getElementById('btnContainer');

let newLabel = document.createElement('p');
newLabel.textContent = "0번 클릭됐습니다!";
buttonContainer.appendChild(newLabel);
let clickCount = 0;

function handleClick(event){
    // 배경 색깔 변경
    const bodyTag = document.getElementsByTagName("body")[0];
    let bodyColor =  bodyTag.style.backgroundColor;
    if (bodyColor == "darkcyan"){
        bodyTag.style.backgroundColor = "#f0f0f0";
    } else {
        bodyTag.style.backgroundColor = "darkcyan";
    }
 
    // 클릭할 때마다 숫자 올리기
    clickCount += 1;
    newLabel.textContent = clickCount + "번 클릭됐습니다!";
}

// 모달 스크립트
let modal = document.getElementById("MyModal"); 
let btn = document.getElementById("myBtn");
let span = document.getElementsByClassName("close")[0];

btn.onclick = function(){
    modal.style.display = "block";
}

span.onclick = function(){
    modal.style.display = "none";
}

window.onclick = function(evnet){
    // 모달 화면 바깥이 눌리면 닫겠다
    if(evnet.target == modal){
        modal.style.display = "none";
    }
}