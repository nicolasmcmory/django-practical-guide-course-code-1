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
    # Helper method to check if a post is stored for later reading
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            return post_id in stored_posts
        return False

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=post).order_by("-date")[:3]
        post_form = PostForm(instance=post)
        comment_form = CommentForm()
        is_saved_for_later = self.is_stored_post(request, post.id)

        return render(
            request,
            "posts/post_detail.html",
            {
                "post": post,
                "form": post_form,
                "comment_form": comment_form,
                "comments": comments,
                "is_saved_for_later": is_saved_for_later,
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
            {
                "post": post,
                "form": post_form,
                "comment_form": comment_form,
                "is_saved_for_later": self.is_stored_post(request, post.id),
            },
        )


class Posts(View):
    def get(self, request):
        posts = Post.objects.all().order_by("-date")[:3]
        return render(request, "posts/posts.html", {"posts": posts})


class ReadLater(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None or len(stored_posts) == 0:
            context = {
                "posts": [],
                "has_posts": False,
            }
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context = {
                "posts": posts,
                "has_posts": True,
            }

        return render(request, "posts/stored_posts.html", context)

    def post(self, request):
        post_id = int(request.POST.get("post_id"))
        stored_posts = request.session.get("stored_posts", [])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(post_id)
            request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect(reverse("posts"))
