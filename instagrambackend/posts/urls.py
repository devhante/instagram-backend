from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views


urlpatterns = [
    path('signup/', views.SignUp.as_view()),
    path('login/', views.Login.as_view()),
    path('posts/', views.PostList.as_view()),
    path('images/', views.ImageList.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('replies/', views.ReplyList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)