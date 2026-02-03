from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_landing, name="blog_landing"),
    path("posts/", views.posts_all, name="posts"),
    path("posts/<slug:post_slug>/", views.blog_post, name="blog_post"),
]
