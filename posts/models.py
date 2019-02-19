from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.CharField(max_length=2200)
    date = models.DateField(default=timezone.now)
    favor = models.BooleanField(default=False)


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    image = models.ImageField(default='default_image.png')


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    content = models.CharField(max_length=2200)
    date = models.DateField(default=timezone.now)


class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    content = models.CharField(max_length=2200)
    date = models.DateField(default=timezone.now)
