from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.shortcuts import render


# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


def google_login(request):
    print("입장")
    return render(request, "index.html")


def google_login_success(request):
    return render(request, "success.html")
