
from django.db import models
from django.db.models import CASCADE

from skymarket.settings import MEDIA_ROOT
from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to=MEDIA_ROOT, null=True, blank=True)

    class Meta:
        ordering = ["created_at"]


class Comment(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=CASCADE)
    ad = models.ForeignKey(Ad, on_delete=CASCADE)
