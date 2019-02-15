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
