from django.shortcuts import render
from .models import TODO
from .serializers import TODOSerializer
from rest_framework import viewsets


class TODOViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
