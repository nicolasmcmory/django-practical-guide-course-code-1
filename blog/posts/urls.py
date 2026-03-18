from django.urls import path
from . import views

urlpatterns = [
    path("", views.Posts.as_view(), name="posts"),
    path("post/", views.CreatePost.as_view(), name="post"),
    path("post/<str:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
