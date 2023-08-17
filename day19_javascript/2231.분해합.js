// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = "216";
const N= parseInt(input);
let M = 0;

for (let i=1; i<=N; i++){    
    const stringI = i.toString();
    let val = i;

    for(let j=0; j < stringI.length; j++){
        val += parseInt(stringI[j]);
    }

    if (val == N){
        M = val;
        break;
    }
}

console.log(M);