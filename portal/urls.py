from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UsersView.as_view(), name="users"),
    path("users/new/", views.NewUserView.as_view(), name="new_user"),
]
