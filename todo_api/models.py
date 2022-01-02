from django.db import models
from django.db.models import deletion

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=50)

class Task(models.Model):
    Title = models.CharField(max_length=50, null=False)
    Description = models.TextField(max_length=1000)
    Completed = models.BooleanField(null=False)
    CreatedOn = models.DateTimeField(auto_now_add=True, null=False)
    CompletedOn = models.DateTimeField()
    BelongsTo = models.ForeignKey(
        User,
        on_delete=deletion.CASCADE,
    )
