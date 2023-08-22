from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login  # 로그인 함수
from django.contrib.auth.forms import (
    UserCreationForm,
)  # 장고가 제공하는 사용자에 대한 기본 양식(아이디, 비밀번호) 생성


def social_login_view(request):
    return render(request, "boardapp/social_login.html")


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "boardapp/article_list.html", {"articles": articles})


def article_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        Article.objects.create(title=title, content=content)
        return redirect("article_list")

    return render(request, "boardapp/article_create.html")


def signup(request):
    # 회원가입 버튼을 눌렀을 때
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        # 만약 폼이 전부 다 잘 입력되었다면
        if form.is_valid():
            user = form.save()  # 저장
            login(request, user)  # 로그인 시켜주기
            return redirect("article_list")

    # url 경로를 타고 맨 처음에 회원가입 페이지를 들어왔을 때
    else:
        form = UserCreationForm()

    return render(request, "boardapp/signup.html", {"form": form})
