from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_landing, name="blog-landing"),
    path("posts/", views.posts_all, name="posts"),
    path("posts/<slug:slug>/", views.blog_post, name="blog-post"),
]
