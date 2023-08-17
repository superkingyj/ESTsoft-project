// function A(callback){
//     callback();
// }

// function B(){
//     console.log("나는 B함수야.");
// }

// A(B);


function findUser(id, cb){
    const user = {
        id: id,
        name: "User" + id,
        email: id + "@test.com"
    };
    cb(user);
}


findUser(1, function(user){
    console.log("user: ", user);
});
