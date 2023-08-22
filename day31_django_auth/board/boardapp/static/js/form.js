document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        const title = document.querySelector('input[name="title"]').value;
        const content = document.querySelector('textarea[name="content"]').value;

        if (title.trim() === "" || content.trim() === "") {
            alert("제목과 내용은 필수 입력 사항입니다.");
            e.preventDefault();
        }
    });
});
