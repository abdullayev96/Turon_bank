from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class FileAPI(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer







