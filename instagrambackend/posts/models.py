from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Post(models.Model):
    content = models.CharField(max_length=5000)
    favor = models.BooleanField(default=False)


class Image(models.Model):
    post_id = models.IntegerField(default=0)
    index = models.IntegerField(default=0)
    