function squareWithCallback(number, callback) {
    if (typeof number !== "number") {
        const error = new Error("유효하지 않은 변수입니다");
        callback(error, undefined);
    } else {
        const result = number * number;
        callback(null, result);
    }
}

function callbackFunction(error, result) {
    if (error) {
        console.log('에러:', error);
    } else {
        console.log('결과:', result);
    }

}

// squareWithCallback(4, callbackFunction);
// squareWithCallback('hi', callbackFunction);


function makeTenWithPromise(number) {
    return new Promise((resolve, reject) => {
        if (typeof number !== 'number'){
            reject(new Error('유효하지 않은 숫자입니다.'));
        } else {
            const amountToAdd = 10-number;
            resolve(amountToAdd);
        }
    });
}

makeTenWithPromise(5)
    .then((amount) => {
        console.log('더해야 하는 값: ', amount);
    })
    .catch((error) => {
        console.log('에러: ', error);
    })