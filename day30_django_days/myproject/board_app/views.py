from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "board_app/article_list.html", {"articles": articles})


def article_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        # create를 하면서 save가 되므로 save 불필요
        Article.objects.create(title=title, content=content)
        return redirect("article_list")

    return render(request, "board_app/article_create.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("article_list")
    else:
        form = UserCreationForm()
    return render(request, "board_app/register.html", {"form": form})
