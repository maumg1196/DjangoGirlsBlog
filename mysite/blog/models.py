from django.db import models
from django.utils import timezone


class Post(models.Model):
    """docstring for Post"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateField(default=timezone.now)
    published = models.DateField(blank=True, null=True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.title