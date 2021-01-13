from rest_framework import serializers
from .models import Stadup, Smile


class StadupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadup
        fields = ('id', 'group', 'user_name', 'done', 'todo', 'problems', 'publication')


class SmileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smile
        fields = ('id', 'group', 'user_name', 'before', 'after', 'publication')