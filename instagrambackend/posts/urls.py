from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views


urlpatterns = [
    path('signup', views.SignUp.as_view()),
    path('login/', views.Login.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)