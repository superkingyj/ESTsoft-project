/*
1. sum에 값이 계속 갱신되어야 하므로 const sum을 let sum으로 변경합니다.
2. 1부터 100까지의 합을 더하는 것이므로 i <= end으로 변경합니다.
3. $sum이라는 문자열이 아니라 sum의 값을 출력하는 것이므로 "를 `으로 변경합니다.
*/
const end = 100;
let sum = 0;

for (let i=1; i <= end; i++){
   if (end % 2 === 0){
       sum += i;
   }
}

console.log(`전체 합은 ${sum}입니다.`);