from django.urls import path

from .views import StadupAPIView

urlpatterns = [
    path('add/', StadupAPIView.as_view()),
]

