const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

class HttpError extends Error {
    constructor(response) {
        super(`${response.status} for ${response.url}`);
        this.name = 'HttpError';
        this.response = response;
    }
}

function loadJson(url){
    return fetch(url).then(response => {
        if(response.status == 200){
            return response.json();
        } else {
            throw new HttpError(response);
        }
    });
}

function demoGithubUser(){
    rl.question("Github username을 입력하세요.", (name) => {
        return loadJson(`https://api.github.com/users/${name}`)
        .then(user => {
            console.log(`이름: ${user.name}`);
            return user;
        })
        .catch(err => {
            if(err instanceof HttpError && err.response.status == 404){
                console.log("일치하는 사용자가 없습니다. 다시 입력해주세요.");a
                return demoGithubUser();
            } else {
                throw err;
            }
        })
    })
}

demoGithubUser();