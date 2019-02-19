from posts.models import User
from posts.models import Post
from posts.models import Image
from posts.models import Comment
from posts.models import Reply
from posts.serializers import UserSerializer
from posts.serializers import PostSerializer
from posts.serializers import ImageSerializer
from posts.serializers import CommentSerializer
from posts.serializers import ReplySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SignUp(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.filter(username=serializer.data['username'])
            except User.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            if user[0].password == serializer.data['password']:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            obj = Post.objects.filter(id=serializer.data['id'])
            obj.delete()
            return Response(stastus=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ImageList(APIView):
    def get(self, request, format=None):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            obj = Image.objects.filter(id=serializer.data['id'])
            obj.delete()
            return Response(stastus=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentList(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            obj = Comment.objects.filter(id=serializer.data['id'])
            obj.delete()
            return Response(stastus=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ReplyList(APIView):
    def get(self, request, format=None):
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            obj = Reply.objects.filter(id=serializer.data['id'])
            obj.delete()
            return Response(stastus=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)