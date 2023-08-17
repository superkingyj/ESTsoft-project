try {
    // const negativeIndex = -1;
    // const array = [1,2,3];
    // console.log(array[negativeIndex]);
    throw new Error('에러가 발생했습니다!');
} catch (error) {
    console.log(error.message);
}
console.log("잘 되네요!");