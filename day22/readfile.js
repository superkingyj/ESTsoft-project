const fs = require('fs');
fs.readFile('./file.txt', 'utf8', (err, data) => {
    if (err){
        console.error(err);
        return;
    }
    console.log('File content: ', data);
});