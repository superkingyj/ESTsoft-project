$(document).ready(function() {
    $("#chageTextBtn").click(function() {
        $("#myHeading").text('안녕하세요, 강의 페이지입니다.');
    });
    
    $('#chageColorBtn').click(function () {
        $("#myHeading").css('color', 'skyblue');
    });
    
    $('#addClassBtn').click(function () {
        $("#myHeading").addClass('highlight');
        $('.highlight').css('color', 'yellow');
    });

    $('#removeClassBtn').click(function () {
        $('#myHeading').removeClass('highlight');
    });

    $('#hideBtn').click(function() {
        $('#myHeading').hide();
    });

    $('#showBtn').click(function() {
        $('#myHeading').show();
    });
});