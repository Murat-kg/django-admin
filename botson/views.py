from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Stadup
from .serializers import StadupSerializer


class StadupAPIView(ListCreateAPIView):
    queryset = Stadup.objects.all()
    serializer_class = StadupSerializer