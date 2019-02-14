from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Post(models.Model):
    content = models.CharField(max_length=2200)
    favor = models.BooleanField(default=False)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    image = models.ImageField(default='default_image.png')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    content = models.CharField(max_length=2200)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)
    content = models.CharField(max_length=2200)