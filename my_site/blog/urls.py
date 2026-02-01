from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_landing, name="blog_landing"),
    path("<str:post_slug>/", views.blog_post, name="blog_post"),
]
