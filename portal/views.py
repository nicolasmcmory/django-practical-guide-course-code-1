from django import forms
from django.shortcuts import render, redirect, reverse
from django.views import View
from .services.interfaces import UserInterface, PostInterface
from .forms import UserForm, PostForm


class UsersView(View):

    def get(self, request):
        users = UserInterface().get_all_users()
        return render(request, "portal/users.html", {"users": users})


class NewUserView(View):

    def post(self, request):
        user_rw = UserInterface()
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            user_rw.create_user(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                image=form.cleaned_data["image"],
            )
            return redirect(reverse("users"))
        else:
            return render(request, "portal/new_user_form.html", {"form": form})

    def get(self, request):
        return render(request, "portal/new_user_form.html", {"form": UserForm()})


class UserDetailView(View):

    def get(self, request, user_id):
        user_rw = UserInterface()
        user = user_rw.get_user_by_id(user_id)
        return render(request, "portal/user_detail.html", {"user": user})


class NewPostView(View):

    def post(self, request):
        post_rw = PostInterface()
        form = PostForm(request.POST)

        if form.is_valid():
            post_rw.create_post(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                author=form.cleaned_data["author"],
            )
            return redirect(reverse("posts"))
        else:
            return render(request, "portal/new_post_form.html", {"form": form})

    def get(self, request):
        return render(request, "portal/new_post_form.html", {"form": PostForm()})


class PostsView(View):
    def get(self, request):
        post_rw = PostInterface()
        posts = post_rw.get_all_posts()
        return render(request, "portal/posts.html", {"posts": posts})
