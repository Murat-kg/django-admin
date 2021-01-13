from django.urls import path

from .views import StadupAPIView, SmileAPIView

urlpatterns = [
    path('add/', StadupAPIView.as_view()),
    path('up/', SmileAPIView.as_view()),
]

