function wakeup(){
    return console.log("아침에 일어나서 강의 듣기!");
}

function eatLaunch(){
    return new Promise((resolve, reject) => {
            setTimeout(function(){
                const data = "점심시간에 점심먹기";
                resolve(data);
        }, 3000);
    });
}

function endClass(){
    return console.log("강의가 끝났다! 놀아야지!");
}

// 점심이 실행되어야지 endclass가 나오도록 함
async function startDay() {
    wakeup();
    const data = await eatLaunch();
    console.log(data);
    endClass();
}

startDay();