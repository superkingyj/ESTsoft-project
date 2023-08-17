function wakeup(){
    console.log("아침에 일어나서 강의 듣기!");
}

function eatLaunch_promise(){
    return new Promise(function(resolve){
        setTimeout(() => {
            console.log("점심시간에 점심먹기");
            resolve();
        }, 3000);
    });
}

function endClass(){
    console.log("강의가 끝났다! 놀아야지!");
}

// 점심이 실행되어야지 endclass가 나오도록 함
wakeup();
eatLaunch_promise().then(function(){
    endClass();
});

// eatLaunch_promise().then(endClass());