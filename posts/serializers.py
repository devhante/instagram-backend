from rest_framework import serializers
from posts.models import User
from posts.models import Post
from posts.models import Image
from posts.models import Comment
from posts.models import Reply

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'writer', 'content', 'date' 'favor')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'post', 'index', 'image')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'index', 'content', 'date')


class ReplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'comment', 'index', 'content', 'date')