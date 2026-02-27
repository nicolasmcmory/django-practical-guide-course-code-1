from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm


# Create your views here.
def review(request):
    has_error_false = {"has_error": False}
    if request.method == "POST":
        entered_username = request.POST["username"]
        print(entered_username)

        if entered_username == "":
            return render(request, "reviews/review.html", {"has_error": True})

        return HttpResponseRedirect("/thank-you")

    return render(request, "reviews/review.html", has_error_false)


def thank_you(request):
    return render(request, "reviews/thank_you.html")
