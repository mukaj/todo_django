from todo_api.models import Task
from django.contrib.auth.models import User
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'Title', 'Description', 'Completed', 'CreatedOn', 'CompletedOn', 'BelongsTo']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']