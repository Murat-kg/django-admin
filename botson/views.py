from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Stadup, Smile
from .serializers import StadupSerializer, SmileSerializer


class StadupAPIView(ListCreateAPIView):
    queryset = Stadup.objects.all()
    serializer_class = StadupSerializer

class SmileAPIView(ListCreateAPIView):
    queryset = Smile.objects.all()
    serializer_class = SmileSerializer
