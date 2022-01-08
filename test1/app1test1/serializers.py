from django.db import models
from rest_framework import serializers
from .models import Cities

class citySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    month = serializers.CharField(max_length=3)
    utilities = serializers.CharField(max_length=300)