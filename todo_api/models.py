from django.db import models
from django.contrib.auth.models import User
from django.db.models import deletion

# Create your models here.

class Task(models.Model):
    Title = models.CharField(max_length=50, null=False)
    Description = models.TextField(max_length=1000)
    Completed = models.BooleanField(auto_created=False, null=False)
    CreatedOn = models.DateTimeField(auto_now_add=True, null=False)
    CompletedOn = models.DateTimeField(null=True)
    BelongsTo = models.ForeignKey(
        User,
        on_delete=deletion.CASCADE,
    )
