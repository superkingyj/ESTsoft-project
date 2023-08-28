from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def login(request):
    return render(request, "login.html")

def main(request):
    username = request.user
    request.user
    return render(request, "main.html", {"username": username})

def logout_view(request):
    logout(request)
    return redirect("login")
