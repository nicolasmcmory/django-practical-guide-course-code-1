from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .services import Posts

# Global posts service instance
posts = Posts()


# Blog post view
def blog_post(request, post_slug):
    post = posts.get_post(post_slug)
    if not post:
        return Http404("Post not found")
    return render(request, "blog/blog_post.html", {"post": post})


# Blog landing page view
def blog_landing(request):
    recent_posts = posts.get_recent_posts()
    return render(request, "blog/landing.html", {"posts": recent_posts})


# Posts landing handler
def posts_all(request) -> HttpResponseRedirect:
    url_redirect = reverse("blog_landing")
    return HttpResponseRedirect(url_redirect)
