from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title 