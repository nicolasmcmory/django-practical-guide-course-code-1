from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect


# Create your views here.
class CreatePost(View):
    def get(self, request):
        form = PostForm()
        return render(request, "posts/post.html", {"form": form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("posts"))
        return render(request, "posts/post.html", {"form": form})


class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=post).order_by("-date")[:3]
        post_form = PostForm(instance=post)
        comment_form = CommentForm()
        return render(
            request,
            "posts/post_detail.html",
            {
                "post": post,
                "form": post_form,
                "comment_form": comment_form,
                "comments": comments,
            },
        )

    def post(self, request, slug):
        # Handle both post update and comment submission
        # Update the post if the post form is valid
        post = Post.objects.get(slug=slug)
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))

        # Sumit a new comment if the comment form is valid
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Instantiate the comment and associate it with the post
            comment = comment_form.save(commit=False)
            comment.post = post
            # Save the comment to the database
            comment.save()
            # Redirect to the same post detail page to show the new comment
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        return render(
            request,
            "posts/post_detail.html",
            {"post": post, "form": post_form, "comment_form": comment_form},
        )


class Posts(View):
    def get(self, request):
        posts = Post.objects.all().order_by("-date")[:3]
        return render(request, "posts/posts.html", {"posts": posts})
