from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Post


# Blog post view
def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/blog_post.html", {"post": post})


# Blog landing page view
def blog_landing(request):
    return HttpResponse("posts")


# Posts landing handler
def posts_all(request) -> HttpResponseRedirect:
    url_redirect = reverse("blog-landing")
    return HttpResponseRedirect(url_redirect)
