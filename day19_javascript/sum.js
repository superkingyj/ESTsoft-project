let sum = 0;

for(let i=1; i <= 100; i++){
    sum += i;
}
console.log(sum);


let numbers = [1,2,3,4,5];

// 배열에 값 추가
numbers.push(6);
console.log(numbers);

// 맨 앞에 값 삭제
numbers.pop()
console.log(numbers);

// 배열의 길이 가져오기
console.log(numbers.length);

// 인덱스로 가져오기
console.log(numbers[2]);

// 해당 인덱스 값 삭제
numbers.splice(1, 2);
console.log(numbers);

// 슬라이싱
let splice_num = numbers.splice(1, 2);
console.log(splice_num);

let sum_eval = 0;
for(let i=1; i <= 1000; i++){
    if(i%2 == 0){
        sum_eval += i;
    }
}
console.log(sum_eval);


let nums = [43, 27, 81, 12, 75, 69, 34, 59, 46, 32, 55, 18, 8, 65, 91, 95, 79, 64, 51, 63];

for(let i = 0; i < nums.length; i++){
    if (nums[i] % 3 == 0){
        console.log(nums[i]);
    }
}