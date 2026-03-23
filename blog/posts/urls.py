from django.urls import path
from . import views

urlpatterns = [
    path("", views.Posts.as_view(), name="posts"),
    path("post/", views.CreatePost.as_view(), name="create_post"),
    path("post/<str:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("read-later/",views.ReadLater.as_view(), name="read_later"),
]
