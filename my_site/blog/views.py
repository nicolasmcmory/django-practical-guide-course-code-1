from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Post, Author


# Blog post view
def blog_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    captions = ", ".join([f"{tag.name}" for tag in post.caption.all()])

    return render(request, "blog/blog_post.html", {"post": post, "captions": captions})


# Blog landing page view
def blog_landing(request):
    posts = Post.objects.all().order_by("-published_date")[:3]
    return render(request, "blog/landing.html", {"posts": posts})


# Posts landing handler
def posts_all(request) -> HttpResponseRedirect:
    url_redirect = reverse("blog-landing")
    return HttpResponseRedirect(url_redirect)


def author(request, first_name):
    related_author = Author.objects.get(first_name=first_name)
    return render(request, "blog/author.html", {"author": related_author})
