const readline = require('readline');

class Game {
    constructor(){
        this.computerChoices = ["가위", "바위", "보"];
    }

    getComputerChoice(){
        const randomIndex = Math.floor(Math.random() * this.computerChoices.length);
        return this.computerChoices[randomIndex];

    }

    play(userChoice){
        const computerChoice = this.getComputerChoice();
        console.log(`플레이어의 선택: ${userChoice}`);
        console.log(`컴퓨터의 선택: ${computerChoice}`);

        if(userChoice == computerChoice){
            console.log("비겼습니다.");
        } else if (
            (userChoice === "가위" && computerChoice === "보") ||
            (userChoice === "바위" && computerChoice === "가위") ||
            (userChoice === "보" && computerChoice === "바위") 
        ) {
            console.log("사용자가 이겼습니다. 🙋.oO(Easy~)");
        } else{
            console.log("컴퓨터가 이겼습니다. 🖥.oO(Easy~) ");
        }
    }
}

const game = new Game();
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const askQuestion = () => {
    rl.question('가위, 바위, 보 중에 하나를 선택하세요. (종료하려면 "종료" 입력) ', (answer) => {
        if (answer === "종료"){
            rl.close();
        }else{
            console.log(game.play(answer));
            askQuestion();
        }
    })
}

askQuestion();