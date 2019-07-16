from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.TextField()
    context = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    update_ip = models.CharField(max_length=15)
    create_ip = models.CharField(max_length=15)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    context = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    update_ip = models.CharField(max_length=15)
    create_ip = models.CharField(max_length=15)
