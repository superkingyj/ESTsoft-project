// 1000이 1초임
// console.log("안녕하세요!");

// setTimeout(() => {
//     console.log("타임아웃! 5초");
// }, 5000);

// setTimeout(() => {
//     console.log("타임아웃! 3초");
// }, 3000);

// console.log("반갑습니다.");


function findUser(id, cb){
    setTimeout(function (){
        const user = {
            id: id,
            name: "User" + id,
            email: id + "@test.com"
        };
        cb(user);
    }, 1000);
}

findUser(1, function(user){
    // 그 다음에 출력
    console.log("user: ", user);
});

// 먼저 출려 
console.log("finish");