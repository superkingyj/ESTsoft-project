from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "board/article_list.html", {"articles": articles})

def article_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        Article.objects.create(title=title, content=content)
        return redirect("article_list")

    return render(request, "board/article_create.html")

def login(request):
    return render(request, "board/login.html")

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("article_list")
    else:
        form = UserCreationForm()

    return render(request, "board/sign_up.html", {"form": form})

def login_success(request):
    print(request)
    username = request.user
    return render(request, "board/article_list.html", {"username": username})

def logout_view(request):
    logout(request)
    return redirect('login')
