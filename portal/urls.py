from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UsersView.as_view(), name="users"),
    path("users/new/", views.NewUserView.as_view(), name="new_user"),
    path("users/<int:user_id>/", views.UserDetailView.as_view(), name="user_detail"),
    path("posts/new/", views.NewPostView.as_view(), name="new_post"),
    path("posts/", views.PostsView.as_view(), name="posts"),
]
