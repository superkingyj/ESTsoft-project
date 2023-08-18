from django.shortcuts import render, redirect
from .models import Post, User
from datetime import date, datetime, timezone, timedelta


# Create your views here.
def read_Post_data(request):
    # posts = Post.objects.filter(published_date__range=(start_date, today))
    posts = Post.objects.all()
    return render(request, "board/index.html", {"posts": posts})


def add_Post_data(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        published_date = request.POST["published_date"]

        post = Post(title=title, content=content, published_date=published_date)
        post.save()
        return redirect("index")

    return render(request, "board/add_page.html")


def add_User_data(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        email = request.POST["email"]
        password = request.POST["password"]
        desc = request.POST["desc"]

        post = User(user_id=user_id, email=email, password=password, desc=desc)
        post.save()

        return redirect("add_user_data_success")

    return render(request, "board/add_my_info.html", {"img": "./static/introduce.png"})


def add_User_data_success(request):
    return render(request, "board/add_my_info_success.html")
