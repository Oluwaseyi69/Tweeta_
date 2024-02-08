import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['last_updated']


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)


