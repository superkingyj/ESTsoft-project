from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
import nltk
import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download()ㅗ


def chat(request):
    if request.method == "POST":
        print("submit")
        user_input = request.POST.get("user_input")
        chatbot = ChatBot(**settings.CHATTERBOT)
        response = chatbot.get_response(user_input)
        return render(
            request,
            "chatbot_app/chat.html",
            {"user_input": user_input, "response": response},
        )

    return render(request, "chatbot_app/chat.html")
