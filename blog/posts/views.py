from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm


# Create your views here.
class CreatePost(View):
    def get(self, request):
        return render(request, "posts/post.html")

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "posts/post.html", {"form": form})
        return render(request, "posts/post.html", {"form": form})


class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "posts/post_detail.html", {"post": post})


class Posts(View):

    posts = Post.objects.all()

    def get(self, request):
        return render(request, "posts/posts.html", {"posts": self.posts})
