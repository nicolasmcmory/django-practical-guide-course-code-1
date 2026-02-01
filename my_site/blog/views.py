from django.shortcuts import render
from django.http import HttpResponse
from .services import Posts

# Global posts service instance
posts = Posts()


# Blog post view
def blog_post(request, post_slug):
    post = posts.get_post(post_slug)
    if post:
        content = post.get("content", "No content available.")
    else:
        content = "Post not found."
    return render(request, "blog/blog_post.html", {"post": post, "content": content})


# Blog landing page view
def blog_landing(request):
    return render(request, "blog/landing.html", {"posts": posts.get_posts()})
