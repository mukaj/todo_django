from todo_api.models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'Title', 'Description', 'Completed', 'CreatedOn', 'CompletedOn', 'BelongsTo']