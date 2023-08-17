from django.shortcuts import render
import datetime as dt


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def new_page(request):
    return render(request, "main/oreumi_page.html")


def new_page2(request):
    return render(request, "main/oreumi_page2.html")


def my_page(request):
    datas = {
        "data": {
            "image_src": "./static/IMG_9486.JPG",
            "infos": ["yujin kim", "cat / lila / 7", "I'm sleepy"],
            "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "visit_count": 1,
            "title": "This is title",
            "date": dt.datetime.now(),
        }
    }
    return render(request, "main/my_page.html", datas)
