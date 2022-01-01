from django.db import models
from django.db.models import deletion

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=50)

class Task(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField(max_length=1000)
    Completed = models.BooleanField()
    CreatedOn = models.DateTimeField(auto_now_add=True)
    CompletedOn = models.DateTimeField()
    BelongsTo = models.ForeignKey(
        User,
        on_delete=deletion.CASCADE,
    )
