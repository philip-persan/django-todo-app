from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Task


class TaskSerializer(ModelSerializer):
    user = serializers.CharField()
    description = serializers.CharField()
    date_created = serializers.DateTimeField()
    date_completed = serializers.DateTimeField(required=False)
    completed = serializers.BooleanField(required=False)

    class Meta:
        model = Task
        fields = '__all__'
