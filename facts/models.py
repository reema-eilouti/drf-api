from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Fact(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)