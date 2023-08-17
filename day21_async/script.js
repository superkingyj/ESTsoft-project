function loadMovieInfo(){
    let movieTitle = document.getElementById("movieTitle").value; // 영화 제목 가져옴
    if (movieTitle === ''){
        alert('영화 제목을 입력해주세요.');
        return;
    }

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(){
        if (xhr.readyState === XMLHttpRequest.DONE){
            if (xhr.status === 200){
                let data = JSON.parse(xhr.responseText)
                if (data.Response === 'False'){
                    alert('영화 정보를 가져오는데 실패했습니다.');
                } else{
                    let movieInfo = '';
                    movieInfo += '<h2>' + data.Title + '</h2>';
                    movieInfo += '<p><strong>장르:</strong>'+ data.Genre + '</p>';
                    movieInfo += '<p><strong>감독:</strong>'+ data.Director + '</p>';
                    movieInfo += '<p><strong>배우:</strong>'+ data.Actors + '</p>';
                    document.getElementById('movieInfo').innerHTML = movieInfo;
                }
            } else {
                alert('영화 정보를 가져오는데 실패했습니다.');
            }
        } 
    };
    xhr.open('GET', 'http://www.omdbapi.com/?i=tt3896198&apikey=7ae3f7bb&t=' + encodeURIComponent(movieTitle), true);
    xhr.send();
}